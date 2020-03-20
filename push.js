var push = require('web-push')

let vapidKeys = {
    publicKey: 'BPsIqVfCuke-WXVfHgaKQupC2e0_m2GevdDDhdRp_cABo1N5bRJN4E1JGL3k1loI8AVE9vA9jeOsarJTZ8MF8gw',
    privateKey: 'T8rhqYL_FSgyi9iePkwwwZlNeJ1joCb2OV9kkxol-0I'    
  }

push.setVapidDetails('mailto:test@code.co.uk', vapidKeys.publicKey, vapidKeys.privateKey)

let sub= {};

push.sendNotification(sub, 'test message')