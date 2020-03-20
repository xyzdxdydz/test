var push = require('web-push')

let vapidKeys = {
    publicKey: 'BPsIqVfCuke-WXVfHgaKQupC2e0_m2GevdDDhdRp_cABo1N5bRJN4E1JGL3k1loI8AVE9vA9jeOsarJTZ8MF8gw',
    privateKey: 'T8rhqYL_FSgyi9iePkwwwZlNeJ1joCb2OV9kkxol-0I'    
  }

push.setVapidDetails('mailto:test@code.co.uk', vapidKeys.publicKey, vapidKeys.privateKey)

let sub={
    endpoint:
    "https://fcm.googleapis.com/fcm/send/cb3R1rE_N6Q:APA91bFspfxsrFbk_vGvuaOZrsEwM378Jus8B7VOCGxPLaJIa78BYlBJ4NOekRJwgrzDUuA-0daWV-zpqwOhXmw7AAsbQhiVSt5rHE2816n4tDkPEhLWdLY-Z7he8SpY-xKwENyd3gbV",
    expirationTime:null,
    keys:{p256dh:"BCFzmKMhkbXPtm9fr2Hl_fTpTyYZSNUWN3cc9gLXVd4WfWviHv64oNzeb8NQIEmqpZuAa0dJQQG9ADhIgn00BsA",auth:"avuX5OtvLlHZZWmKhbIFTg"
    }
};

push.sendNotification(sub, 'test message')