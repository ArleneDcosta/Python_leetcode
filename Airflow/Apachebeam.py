import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

class ParseLogEntry(beam.DoFn):
    def process(self, element):
        import re
        # Example log format: "INFO 2024-06-16 12:34:56,789 myapp.views Some log message"
        pattern = re.compile(r'(\w+) (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) (.+)')
        match = pattern.match(element)
        if match:
            log_level, timestamp, message = match.groups()
            yield {
                'log_level': log_level,
                'timestamp': timestamp,
                'message': message
            }

class FilterLogLevel(beam.DoFn):
    def __init__(self, level):
        self.level = level

    def process(self, element):
        if element['log_level'] == self.level:
            yield element

def run():
    pipeline_options = PipelineOptions()
    
    with beam.Pipeline(options=pipeline_options) as p:
        logs = (
            p
            | 'ReadLogs' >> beam.io.ReadFromText('path/to/django_logs.log')
            | 'ParseLogEntries' >> beam.ParDo(ParseLogEntry())
        )
        
        info_logs = (
            logs
            | 'FilterInfoLogs' >> beam.ParDo(FilterLogLevel('INFO'))
        )
        
        error_logs = (
            logs
            | 'FilterErrorLogs' >> beam.ParDo(FilterLogLevel('ERROR'))
        )
        
        # Count log levels
        log_counts = (
            logs
            | 'ExtractLogLevels' >> beam.Map(lambda x: x['log_level'])
            | 'CountLogLevels' >> beam.combiners.Count.PerElement()
        )
        
        # Write results to text files
        info_logs | 'WriteInfoLogs' >> beam.io.WriteToText('path/to/output/info_logs')
        error_logs | 'WriteErrorLogs' >> beam.io.WriteToText('path/to/output/error_logs')
        log_counts | 'WriteLogCounts' >> beam.io.WriteToText('path/to/output/log_counts')
        
if __name__ == '__main__':
    run()
