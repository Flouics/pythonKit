import frida
import sys

rdev = frida.get_usb_device()
session = rdev.attach("com.youqing.zongcai.mirror")  # 要hook的apk包名

src = """
Java.perform(function(){
    var mainAc = Java.use("org.cocos2dx.lua.AppActivity");
    mainAc.onResume.overload().implementation = function () {
        send("Hook Start...");
        var arg = arguments[0];
        send("getTest arg:"+arg);
        send("getTest res:"+res);
        return this.onResume();
    }
});
"""
script = session.create_script(src)


def on_message(message, data):
    print(message)
    print(data)


script.on("message", on_message)
script.load()
sys.stdin.read()