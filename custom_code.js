
function loadPageInformationIntoDrift() {
  function convertToDisplayName(snakeCase) {
    var parts = snakeCase.split(‘-’)
    parts = parts.map(function(word) {
      var firstLetter = word.substr(0,1)
      var rest = word.substr(1)
      return firstLetter.toUpperCase() + rest
    })
    return parts.join(' ’)
  }

  var part = location.pathname.split(‘/’)
  var state = part[1]
  var exactLocation = part[2]

  drift.api.setUserAttributes({
   “State Page”: convertToDisplayName(state),
   “Location Page”: convertToDisplayName(exactLocation)
  })

}

drift.on(‘ready’, loadPageInformationIntoDrift())
