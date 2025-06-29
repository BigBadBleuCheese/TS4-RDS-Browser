from sims4.commands import CheatOutput, Command, CommandType
from uuid import UUID

_bridged_ui = None
_bridged_ui_uuid = UUID('d40975ba-d759-402b-9002-a3d449356d01')

@Command("rds_browser.launch", command_type=CommandType.Live)
def command_launch_rds_browser(_connection=None):
    respond_to_player = CheatOutput(_connection)

    global _bridged_ui
    if _bridged_ui is not None:
        respond_to_player("My bridged UI is already open in PlumbBuddy.")
        _bridged_ui.focus()
        return

    try:
        from plumbbuddy_proxy.asynchronous import await_for, listen_for
        from plumbbuddy_proxy.api import gateway, PlumbBuddyNotConnectedError, PlayerDeniedRequestError, BridgedUiNotFoundError

        def initialize_bridged_ui(bridged_ui):
            global _bridged_ui
            _bridged_ui = bridged_ui

            @listen_for(bridged_ui.destroyed)
            def handle_bridged_ui_destroyed(_):
                global _bridged_ui
                _bridged_ui = None

        @await_for(gateway.look_up_bridged_ui(_bridged_ui_uuid))
        def look_up_bridged_ui_continuation(bridged_ui, fault):
            if bridged_ui:
                respond_to_player("My bridged UI is already open in PlumbBuddy.")
                initialize_bridged_ui(bridged_ui)
                bridged_ui.focus()
                return
            
            if isinstance(fault, PlumbBuddyNotConnectedError):
                respond_to_player("I can't display my bridged UI since you've shutdown PlumbBuddy! Start it back up and try again...")
                return
            
            if not isinstance(fault, BridgedUiNotFoundError):
                respond_to_player(f"I tried to look up a reference to my bridged UI and the look up failed for an unexpected reason: {str(fault)}")
                return
            
            #@await_for(gateway.request_bridged_ui(None, 'http://localhost:3000', _bridged_ui_uuid, 'RDS Browser', 'You typed the command in the game console to get me to make this request.', 'RDS Browser', 'tab-icon.png'))
            @await_for(gateway.request_bridged_ui(__file__, 'ui', _bridged_ui_uuid, 'RDS Browser', 'You typed the command in the game console to get me to make this request.', 'RDS Browser', 'tab-icon.png'))
            def request_bridged_ui_continuation(bridged_ui, fault):
                if bridged_ui:
                    respond_to_player("I've opened my bridged UI in PlumbBuddy.")
                    initialize_bridged_ui(bridged_ui)
                    return
                
                if isinstance(fault, PlumbBuddyNotConnectedError):
                    respond_to_player("I can't display my bridged UI since you've shutdown PlumbBuddy! Start it back up and try again...")
                    return

                if isinstance(fault, PlayerDeniedRequestError):
                    respond_to_player("Well, PlumbBuddy says you denied permission to display my bridged UI. Don't know why you asked...")
                    return
                
                respond_to_player(f"I tried to request a reference to my bridged UI and the request failed for an unexpected reason: {str(fault)}")

    except ModuleNotFoundError:
        respond_to_player("I couldn't find the PlumbBuddy Proxy, so... you may need to download and run PlumbBuddy from https://plumbbuddy.app -OR- you've turned off runtime integration in PlumbBuddy.")
