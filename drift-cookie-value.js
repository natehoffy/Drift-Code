function getCookie(cname) { // Simple getCookie utility stolen from https://www.w3schools.com/js/js_cookies.asp
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for(var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

function getValueFromCookie(key) {
    const splitCookie = "; " + document.cookie;
    const cookieKeyValues = splitCookie.split(`; ${key} =`)
    if (cookieKeyValues.length < 2) { return ""; }
    return cookieKeyValues[1]
}

drift.on('ready', function() {
    drift.api.setUserAttributes({
        custom_cookie_field_in_Drift: getCookie('name_of_cookie_to_get')
    });
    console.log(getCookie('name_of_cookie_to_get'))
}); 