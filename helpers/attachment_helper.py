def get_attachments_in_str(attachments):
    att_str = []
    for att in attachments:
        if att.photo:
            att_str.append(f'photo{att.photo.owner_id}_{att.photo.id}')
        if (att.gift):
            att_str.append(f'gift{att.gift.owner_id}_{att.gift.id}')
        if (att.doc):
            att_str.append(f'doc{att.doc.owner_id}_{att.doc.id}')
        if (att.video):
            att_str.append(f'video{att.video.owner_id}_{att.video.id}')
        if (att.audio):
            att_str.append(f'audio{att.audio.owner_id}_{att.audio.id}')
        if (att.link):
            att_str.append(f'link{att.link.owner_id}_{att.link.id}')

    return att_str
