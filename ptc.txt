<!-- Start of Async Drift Code -->
<script>
"use strict";

!function() {
  var t = window.driftt = window.drift = window.driftt || [];
  if (!t.init) {
    if (t.invoked) return void (window.console && console.error && console.error("Drift snippet included twice."));
    t.invoked = !0, t.methods = [ "identify", "config", "track", "reset", "debug", "show", "ping", "page", "hide", "off", "on" ],
    t.factory = function(e) {
      return function() {
        var n = Array.prototype.slice.call(arguments);
        return n.unshift(e), t.push(n), t;
      };
    }, t.methods.forEach(function(e) {
      t[e] = t.factory(e);
    }), t.load = function(t) {
      var e = 3e5, n = Math.ceil(new Date() / e) * e, o = document.createElement("script");
      o.type = "text/javascript", o.async = !0, o.crossorigin = "anonymous", o.src = "https://js.driftt.com/include/" + n + "/" + t + ".js";
      var i = document.getElementsByTagName("script")[0];
      i.parentNode.insertBefore(o, i);
    };
  }
}();
drift.SNIPPET_VERSION = '0.3.1';
drift.load('fs4rizkxmwrp');

drift.on(‘ready’, function (api) {

      function getRefQueryParam(name) {
          name = name.replace(/[\[]/, ‘\\[‘).replace(/[\]]/, ‘\\]‘);
          var regex = new RegExp(‘[\\?&]’ + name + ‘=([^&#]*)‘);
          var results = regex.exec(location.search);
          return results === null ? ‘’ : decodeURIComponent(results[1].replace(/\+/g, ' '));
      }


      const PROPS = [
          ‘elqCampaignId’,
      ]

      const numVisits = parseInt(localStorage.getItem(‘Drift.Targeting.numberOfVisits’))
      const currentSession = parseInt(localStorage.getItem(‘Drift.Targeting.numberOfSessions’))
      const lastSession = parseInt(localStorage.getItem(‘lastDriftSessionNumber’))

      let newSession = false
      if (!lastSession || !currentSession || currentSession > lastSession) {
          newSession = true
      }

      localStorage.setItem(‘lastDriftSessionNumber’, currentSession)

      const attrs = {}
      PROPS.map(prop => {
          const value = getRefQueryParam(prop)
          let propName = ‘’
          if (numVisits === 1) {
              propName = ‘original_’ + prop
              attrs[propName] = value
          }

          if (newSession) {
              propName = ‘recent_’  + prop
              attrs[propName] = value
          }
      })

      if (Object.keys(attrs).length > 0) {
          // console.log(‘set attrs’, attrs)
          drift.api.setUserAttributes(attrs)
      }

      // Set on email capture.
      window.drift.on(‘emailCapture’, function(e) {
          const emailAttrs = {}
          PROPS.map(prop => {
              const value = getRefQueryParam(prop)
              const propName = “conversion_” + prop
              emailAttrs[propName] = value
          });
          // console.log(‘set emailAttrs’, emailAttrs)
          drift.api.setUserAttributes(emailAttrs)
      });

  });

</script>
<!-- End of Async Drift Code -->
