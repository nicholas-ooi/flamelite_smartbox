App.info({
  id: 'com.flamelite.smartbox',
  name: 'Flamelite SmartBox',
  description: 'Flamelite SmartBox',
  author: 'Electros Consultancy',
  email: 'contact@example.com',
  website: 'http://example.com'
});
// Set PhoneGap/Cordova preferences
App.setPreference('BackgroundColor', '0xff0000ff');
App.setPreference('HideKeyboardFormAccessoryBar', true);
App.setPreference('Orientation', 'default');
App.setPreference('StatusBarOverlaysWebView', 'true');
App.setPreference('StatusBarStyle', 'lightcontent');

// Add custom tags for a particular PhoneGap/Cordova plugin
// to the end of generated config.xml.
// Universal Links is shown as an example here.
App.appendToConfig(`
  <universal-links>
    <host name="localhost:3000" />
  </universal-links>
`);

App.accessRule('*');
