// Start of Marketo Code
<script type="text/javascript">
    (function() {
      var didInit = false;
      function initMunchkin() {
        if(didInit === false) {
          didInit = true;
          Munchkin.init('844-RKG-112');
        }
      }
      var s = document.createElement('script');
      s.type = 'text/javascript';
      s.async = true;
      s.src = '//munchkin.marketo.net/munchkin.js';
      s.onreadystatechange = function() {
        if (this.readyState == 'complete' || this.readyState == 'loaded') {
          initMunchkin();
        }
      };
      s.onload = initMunchkin;
      document.getElementsByTagName('head')[0].appendChild(s);
    })();

    //Function to read value of a cookie
function readCookie(name) {
    var cookiename = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(cookiename) == 0) return c.substring(cookiename.length,c.length);
    }
    return null;
}
 
//Call readCookie function to get value of user's Marketo cookie
var value = readCookie('_mkto_trk');
    </script>
// End of Marketo Code