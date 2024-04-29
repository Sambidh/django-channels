from channels.generic.websocket import AsyncWebsocketConsumer
import json

class DashboardConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        dashboard_slug = self.scope['url_route']['kwargs']['dashboard_slug']
        self.dashboard_slug - dashboard_slug
        self.room_group_name = f'stats-{dashboard_slug}'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        print(f'connection closed with code : {close_code}')

        await self.channel_layer.grooup_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        sender = text_data_json["sender"]

        print(message)
        print(sender)

        await self.channel_layer.group_send(self.room_group_name, {
            'type' : 'statistics_message',
            'message' : message,
            'sender' : sender,

        })

        await self.send(text_data=json.dumps({
            'message' : 'hello darkness my old friend',
            # 'sender' : sender
        }))

    async def statistics_message(self, event):
        message = event['message']
        sender = event['sender']

        await self.send(text_data = json.dumps(
            {
                'message' : message,
                'sender' : sender,
            }
        ))