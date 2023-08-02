import logging
from typing import List # noqa: F401
from alfred_self_service_generators_dc_inter_networks.generators.bfc_pc_span_decom.bfc_span_decom_deployment_options \
import BfcSpanDecommDeploymentOptions
from alfred_self_service_python_helpers import DeploymentPlanBase
from alfred_self_service_python_helpers.core.deployment_plan_phase import Phase  # noqa: F401
from alfred_self_service_python_helpers.core.dpg_options import DPGOptions
from alfred_self_service_python_helpers.core.deployment_plan_decorator import DeploymentPlan
from alfred_self_service_generators_dc_inter_networks.generators.bfc_pc_span_decom.pre_checks import  PreChecks

log = logging.getLogger(__name__)

# TODO - 1) Include RM flip phase as part of DPG 2) Extend the DPG for Ring span decomm 3) Implement NTVS

@DeploymentPlan(name="alfredselfservice.AlfredSelfServiceGeneratorsDCInterNetworks.bfc_pc_span_decom")  # noqa: C901
def bfc_pc_span_decom(dpg_options: DPGOptions) -> DeploymentPlanBase:
         """
         Prechecks to decommission a PC BFC span between two data centers. This DPG will be a migration
         for the prechecks in the Daryl template
         which is being used to decomm a PC bfc span.
     
         """
        
    log.info("Entered the very start of the DPG, function 'bfc_pc_span_decom'")

    plan = DeploymentPlanBase(
        dpg_options=dpg_options,
        description="Prechecks to Decomm BFC-to-BFC PC span between two data centers",
        short_description="Prechecks BFC-BFC pc span decomm",
        summary=str(bfc_pc_span_decom.__doc__)
     )

    options = BfcSpanDecommDeploymentOptions(plan=plan, dpg_options=dpg_options, log=log)

    pre_checks = PreChecks(options=options)
    phases: List[Phase] = []
    phases.extend(pre_checks.roll_forward_phases)
    plan.generate_plan(
    phases=phases,
    additional_devices=options.remote_brick.devices_names,
     container=options.bfc_bfc_sub_span_id_valid_for_swf
    )
    return plan

