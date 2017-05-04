from cloudshell.api.cloudshell_api import InputNameValue
from cloudshell.sandbox.orchestration.sandbox_manager import SandboxManager
from cloudshell.sandbox.orchestration.default_setup_orchestrator import DefaultSetupWorkflow

def load_firmware_sequential(sandbox):
    """
    :param SandboxManager sandbox:
    :return:
    """
    nxso_switches = sandbox.components.get_resources_by_model('nxos')
    for r in nxso_switches:
        sandbox.api.ExecuteCommand(reservationId= sandbox.reservation_id,
                                   targetName=r.FullName,
                                   targetType='Resource',
                                   commandName='load_firemware',
                                   commandInputs=[InputNameValue('fw_version',
                                                                 sandbox.globals['fw_version'])])


sandbox = SandboxManager()
DefaultSetupWorkflow.extend(sandbox)

nxso_switches = sandbox.components.get_resources_by_model('nxos')
sandbox.workflow.add_provisioning_process(function=load_firmware_sequential,
                                          resources= nxso_switches,
                                          steps=['Load Firmware'])

sandbox.execute()