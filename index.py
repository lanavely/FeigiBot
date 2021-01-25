from vkwave.bots import SimpleLongPollBot
from data.peer import Peer
from parsing.parsing import get_schedule
from helpers import data_time_parser
from config import group as group_config

bot = SimpleLongPollBot(tokens=group_config.TOKEN,
                        group_id=group_config.GROUP_ID)

@bot.message_handler(bot.command_filter(["конфигурация", "конфиг", "к"]))
async def handle_config(event: bot.SimpleBotEvent) -> str:
    """Write to the database the schedule link  for the peer"""
    received_message = event.object.object.message
    link = received_message.text.replace("!конфигурация ", "").strip()
    groupNubmer = int(link.rsplit('/', 1)[-1])
    conversation_id = received_message.peer_id
    peer = Peer.get_or_none(vk_user_id=conversation_id)
    if peer:
        peer.group_number = groupNubmer
        peer.save()
    else:
        Peer.create(vk_user_id=conversation_id, group_number=groupNubmer)
    await event.answer("Добавлена ссылка на " + link)

@bot.message_handler(bot.command_filter(["расписание", "расп", "р"]))
async def handle_schedule(event: bot.SimpleBotEvent):
    """Parse and sends the schedule"""
    received_message = event.object.object.message
    splitted_message = received_message.text.split(' ', 1)
    parameter = ''
    if (len(splitted_message) > 1):
        parameter = splitted_message[1].strip()
    user_id = received_message.peer_id
    user = Peer.get_or_none(vk_user_id=user_id)
    if user:
        await event.answer(get_schedule(str(user.group_number), data_time_parser.get_date_by_name(parameter)))
    else:
        await event.answer("Пользователь не сконфигурировал расписание")

bot.run_forever()
