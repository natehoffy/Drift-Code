  <script>
    // Send all Drift events to the console for debugging //
    window.drift.on('ready',function() {console.debug('DRIFT DEBUG: Ready. ', arguments)})
    window.drift.on('startConversation',function() {console.debug('DRIFT DEBUG: startConversation. ', arguments)})
    window.drift.on('message:sent',function() {console.debug('DRIFT DEBUG: messageSent. ', arguments)})
    window.drift.on('message',function() {console.debug('DRIFT DEBUG: messageRecieved. ', arguments)})
    window.drift.on('emailCapture',function() {console.debug('DRIFT DEBUG: emailCapture. ', arguments)})
    window.drift.on('scheduling:requestMeeting',function() {console.debug('DRIFT DEBUG: requestMeeting. ', arguments)})
    window.drift.on('scheduling:meetingBooked',function() {console.debug('DRIFT DEBUG: meetingBooked. ', arguments)})
    window.drift.on('conversation:buttonClicked',function() {console.debug('DRIFT DEBUG: buttonClicked. ', arguments)})
    window.drift.on('sidebarOpen',function() {console.debug('DRIFT DEBUG: sidebarOpen. ', arguments)})
    window.drift.on('sidebarClose',function() {console.debug('DRIFT DEBUG: welcomeMessageOpen. ', arguments)})
    window.drift.on('welcomeMessage:open',function() {console.debug('DRIFT DEBUG: welcomeMessageClose ', arguments)})
    window.drift.on('welcomeMessage:close',function() {console.debug('DRIFT DEBUG: Widget ', arguments)})
    window.drift.on('awayMessage:open',function() {console.debug('DRIFT DEBUG: awayMessageOpen ', arguments)})
    window.drift.on('awayMessage:close',function() {console.debug('DRIFT DEBUG: awayMessageClose ', arguments)})
    window.drift.on('campaign:open',function() {console.debug('DRIFT DEBUG: campaignOpen ', arguments)})
    window.drift.on('campaign:dismiss',function() {console.debug('DRIFT DEBUG: campaignDismiss ', arguments)})
    window.drift.on('campaign:click',function() {console.debug('DRIFT DEBUG: campaignClick ', arguments)})
    window.drift.on('campaign:submit',function() {console.debug('DRIFT DEBUG: campaignSubmit ', arguments)})
    window.drift.on('sliderMessage:open',function() {console.debug('DRIFT DEBUG: sliderMessageOpen ', arguments)})
    window.drift.on('sliderMessage:close',function() {console.debug('DRIFT DEBUG: sliderMessageClose ', arguments)})
  </script>