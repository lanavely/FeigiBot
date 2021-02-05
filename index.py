from vkwave.bots import SimpleLongPollBot
from data.peer import *
from parsing.parsing import get_schedule
from helpers import data_time_parser
from config import group as group_config

bot = SimpleLongPollBot(tokens=group_config.TOKEN,
                        group_id=group_config.GROUP_ID)


@bot.message_handler(bot.command_filter(["к"]))
async def handle_config(event: bot.SimpleBotEvent):
    """Write to the database the schedule link  for the peer"""
    try:
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
    except Exception as e:
        await event.answer("Произошла ошибка, убедитесь в правильности переданных параметров(")
        print(e)


@bot.message_handler(bot.command_filter(["р"]))
async def handle_schedule(event: bot.SimpleBotEvent):
    """Parse and sends the schedule"""
    try:
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
    except Exception as e:
        await event.answer("Произошла ошибка, убедитесь в правильности переданных параметров(")
        print(e)


@bot.message_handler(bot.command_filter("", "#"))
async def handle_hashtag(event: bot.SimpleBotEvent):
    try:
        message = event.object.object.message
        text = message.text[1:].strip().lower()
        if text == "бесплатно":
            await event.answer("За деньги можно и бесплатно поработать")
            return
        if text == "вебинары":
            await event.answer("https://tt.chuvsu.ru/webinar")
            return
        if text.startswith("что по"):
            await event.answer(
                f'Често говоря сам не знаю что по {message.split()[2].replace("?", "")}, но я бы лучше этого не делал и повалялся на диване')
            return
        saved_message = SavedMassagesInText.get_or_none(peer_id=message.peer_id, hashtag=text)
        # atts = Attachments.select().where(peer_id=message.peer_id, hashtag=text)
        if saved_message:
            await event.answer(saved_message.text)
        else:
            await event.answer("На этот хештег ничего нету(")
    except Exception as e:
        await event.answer("Уупс, что пошло не так, убедитесь в правильности переданных параметров(")
        print(e)


@bot.message_handler(bot.command_filter("save", "/"))
async def handle_save(event: bot.SimpleBotEvent):
    try:
        message = event.object.object.message
        if not message.reply_message:
            await event.answer("Уупс, неправильные параметры")
            return
        hashtag = message.text.replace("/save ", "").strip().lower()[:100]
        # attachments = message.reply_message.attachments
        if not hashtag:
            await event.answer("Нету ключа для сохранения")
            return
        saved_message = SavedMassagesInText.get_or_none(peer_id=message.peer_id, hashtag=hashtag)
        if saved_message:
            saved_message.message_id = message.reply_message.conversation_message_id
            saved_message.author_id = message.from_id
            saved_message.text = message.reply_message.text
            # Attachments.delete().where(peer_id=message.peer_id, hashtag=hashtag)
            # att_str = get_attachments_in_str(attachments)
            # for att in att_str:
            #     Attachments.create(peer_id=message.peer_id, hashtag=hashtag, attachment=att)

            saved_message.save()
            return
        else:
            SavedMassagesInText.create(peer_id=message.peer_id,
                                 hashtag=hashtag,
                                 message_id=message.reply_message.conversation_message_id,
                                 author_id=message.from_id,
                                 text = message.reply_message.text)
            # att_str = get_attachments_in_str(attachments)
            # for att in att_str:
            #     Attachments.create(peer_id=message.peer_id, hashtag=hashtag, attachment=att)

            return
    except Exception as e:
        await event.answer("Уупс, что пошло не так, убедитесь в правильности переданных параметров(")
        print(e)


bot.run_forever()
