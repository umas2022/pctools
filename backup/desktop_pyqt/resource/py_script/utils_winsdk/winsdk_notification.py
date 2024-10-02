'''
create: 2023.2.25
使用winsdk包的win10通知显示

'''

import winsdk.windows.ui.notifications as notifications  # pip install winsdk
import winsdk.windows.data.xml.dom as dom


class WinsdkNotification():
    def __init__(self) -> None:
        pass

    def wn_show(self, title, content):
        nManager = notifications.ToastNotificationManager
        notifier = nManager.create_toast_notifier()
        # define your notification as string
        tString = """
        <toast>
            <visual>
                <binding template='ToastGeneric'>
                    <text>%s</text>
                    <text>%s</text>
                </binding>
            </visual>
        </toast>
        """ % (title, content)
        # convert notification to an XmlDocument
        xDoc = dom.XmlDocument()
        xDoc.load_xml(tString)
        notifier.show(notifications.ToastNotification(xDoc))
