window.drift.on('ready', function(api) {
    window.drift.on('message:sent', function(event) {
        {
          _satellite.setVar('driftInteractionCategory', 'drift');
          _satellite.setVar('driftInteractionAction', 'message sent');
          _satellite.setVar('driftInteractionLabel', 'drift>message sent conversation id: ' + event.conversationId);
          _satellite.track('driftInteractionEvent');
        }
    })

    window.drift.on('startConversation', function(event) {
        {
          _satellite.setVar('driftInteractionCategory', 'drift');
          _satellite.setVar('driftInteractionAction', 'start conversation');
          _satellite.setVar('driftInteractionLabel', 'drift>start conversation id: ' + event.conversationId);
          _satellite.track('driftInteractionEvent');
        }
    })

    window.drift.on('emailCapture', function(event) {
        {
          _satellite.setVar('driftInteractionCategory', 'drift');
          _satellite.setVar('driftInteractionAction', 'email capture');
          _satellite.setVar('driftInteractionLabel', 'drift>email capture');
          _satellite.track('driftInteractionEvent');
        }
    })

    window.drift.on('welcomeMessage:open', function(e) {
        {
          _satellite.setVar('driftInteractionCategory', 'drift');
          _satellite.setVar('driftInteractionAction', 'welcome message open');
          _satellite.setVar('driftInteractionLabel', 'drift>welcome message open');
          _satellite.track('driftInteractionEvent');
        }
    })

    window.drift.on('welcomeMessage:close', function(e) {
        {
          _satellite.setVar('driftInteractionCategory', 'drift');
          _satellite.setVar('driftInteractionAction', 'welcome message closed');
          _satellite.setVar('driftInteractionLabel', 'drift>welcome message closed');
          _satellite.track('driftInteractionEvent');
        }
    })

    window.drift.on('sidebarOpen', function(e) {
        {
          _satellite.setVar('driftInteractionCategory', 'drift');
          _satellite.setVar('driftInteractionAction', 'sidebar open');
          _satellite.setVar('driftInteractionLabel', 'drift>sidebar open');
          _satellite.track('driftInteractionEvent');
        }
    })

    window.drift.on('sidebarClose', function(e) {
        {
          _satellite.setVar('driftInteractionCategory', 'drift');
          _satellite.setVar('driftInteractionAction', 'sidebar close');
          _satellite.setVar('driftInteractionLabel', 'drift>sidebar close');
          _satellite.track('driftInteractionEvent');
        }
    })

    window.drift.on('campaign:open', function(event) {
        {
          _satellite.setVar('driftInteractionCategory', 'drift');
          _satellite.setVar('driftInteractionAction', 'campaign open');
          _satellite.setVar('driftInteractionLabel', 'drift>campaign open id: ' + event.campaignId);
          _satellite.track('driftInteractionEvent');
        }
    })

    window.drift.on('campaign:dismiss', function(event) {
        {
          _satellite.setVar('driftInteractionCategory', 'drift');
          _satellite.setVar('driftInteractionAction', 'campaign dismiss');
          _satellite.setVar('driftInteractionLabel', 'drift>campaign dismiss id: '+ event.campaignId);
          _satellite.track('driftInteractionEvent');
        }
    })

    window.drift.on('campaign:click', function(event) {
        {
          _satellite.setVar('driftInteractionCategory', 'drift');
          _satellite.setVar('driftInteractionAction', 'campaign click');
          _satellite.setVar('driftInteractionLabel', 'drift>campaign click id: ' + event.campaignId);
          _satellite.track('driftInteractionEvent');
        }
    })

    window.drift.on('campaign:submit', function(event) {
        {
          _satellite.setVar('driftInteractionCategory', 'drift');
          _satellite.setVar('driftInteractionAction', 'campaign submit');
          _satellite.setVar('driftInteractionLabel', 'drift>campaign submit id: ' + event.campaignId);
          _satellite.track('driftInteractionEvent');
        }
    })

    window.drift.on('scheduling:meetingBooked', function(event) {
        {
          _satellite.setVar('driftInteractionCategory', 'drift');
          _satellite.setVar('driftInteractionAction', 'meeting booked');
          _satellite.setVar('driftInteractionLabel', 'drift>meeting booked');
          _satellite.track('driftInteractionEvent');
        }
    })

    window.drift.on('conversation:selected', function(event) {
        {
          _satellite.setVar('driftInteractionCategory', 'drift');
          _satellite.setVar('driftInteractionAction', 'conversation selected');
          _satellite.setVar('driftInteractionLabel', 'drift>conversation:selected');
          _satellite.track('driftInteractionEvent');
        }
    })

    window.drift.on('message', function(event) {
        {
          _satellite.setVar('driftInteractionCategory', 'drift');
          _satellite.setVar('driftInteractionAction', 'message');
          _satellite.setVar('driftInteractionLabel', 'drift>message');
          _satellite.track('driftInteractionEvent');
        }
    })

    window.drift.on('phoneCapture', function(event) {
        {
          _satellite.setVar('driftInteractionCategory', 'drift');
          _satellite.setVar('driftInteractionAction', 'phoneCapture');
          _satellite.setVar('driftInteractionLabel', 'drift>phoneCapture');
          _satellite.track('driftInteractionEvent');
        }
    })

    window.drift.on('scheduling:requestMeeting', function(event) {
        {
          _satellite.setVar('driftInteractionCategory', 'drift');
          _satellite.setVar('driftInteractionAction', 'scheduling:requestMeeting');
          _satellite.setVar('driftInteractionLabel', 'drift>scheduling:requestMeeting');
          _satellite.track('driftInteractionEvent');
        }
    })

    window.drift.on('conversation:playbookFired', function(event) {
        {
          _satellite.setVar('driftInteractionCategory', 'drift');
          _satellite.setVar('driftInteractionAction', 'conversation:playbookFired');
          _satellite.setVar('driftInteractionLabel', 'drift>conversation:playbookFired');
          _satellite.track('driftInteractionEvent');
        }
        console.log('playbook fired');
    })

    window.drift.on('conversation:playbookClicked', function(event) {
        {
          _satellite.setVar('driftInteractionCategory', 'drift');
          _satellite.setVar('driftInteractionAction', 'conversation:playbookClicked');
          _satellite.setVar('driftInteractionLabel', 'drift>conversation:playbookClicked');
          _satellite.track('driftInteractionEvent');
        }
    })

    window.drift.on('conversation:playbookDismissed', function(event) {
        {
          _satellite.setVar('driftInteractionCategory', 'drift');
          _satellite.setVar('driftInteractionAction', 'conversation:playbookDismissed');
          _satellite.setVar('driftInteractionLabel', 'drift>conversation:playbookDismissed');
          _satellite.track('driftInteractionEvent');
        }
    })

    window.drift.on('conversation:buttonClicked', function(event) {
        {
          _satellite.setVar('driftInteractionCategory', 'drift');
          _satellite.setVar('driftInteractionAction', 'conversation:buttonClicked');
          _satellite.setVar('driftInteractionLabel', 'drift>conversation:buttonClicked');
          _satellite.track('driftInteractionEvent');
        }
    })

    window.drift.on('conversation:firstInteraction', function(event) {
        {
          _satellite.setVar('driftInteractionCategory', 'drift');
          _satellite.setVar('driftInteractionAction', 'conversation:firstInteraction');
          _satellite.setVar('driftInteractionLabel', 'drift>conversation:firstInteraction');
          _satellite.track('driftInteractionEvent');
        }
    })

});
