#!/usr/bin/python

import dbus
import dbus.mainloop.glib
from xml.etree import cElementTree as ct
import sys
import signal
import gobject


def sighand(*args, **kwargs):
    print args, kwargs
    


if __name__=="__main__":
        signal.signal(signal.SIGINT, signal.SIG_DFL)

        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

        sys=dbus.SystemBus()
        obj=sys.get_object("org.freedesktop.systemd1","/org/freedesktop/systemd1")
        mif=dbus.Interface(obj,"org.freedesktop.systemd1.Manager")

        sys.add_signal_receiver(handler_function=sighand)
        lu=mif.ListUnits()

        loop=gobject.MainLoop()
        print loop
        loop.run()


