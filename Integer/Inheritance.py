from collections import Counter


class FancyCounter(Counter):
    def commonest(self):
        print(self.most_common(10))
        (value1, count1), (value2, count2) = self.most_common(10)
        if count1 == count2:
            raise ValueError("No unique most common value")
        return value1



obj = FancyCounter("Hello there!")
obj.commonest()
