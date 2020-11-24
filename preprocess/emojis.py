import re
import emoji

pos_emojis = ['😀', '😁', '😂', '🤣', '😃', '😄', '😆', '😊', '😋', '😎',
 '😍', '😘', '🥰', '😚', '☺️', '🙂', '🤗', '🤩', '😏', '😌', '😛', '😜',
 '😝', '🙃', '🤑', '🤠', '😇', '🥳', '🥺', '😅', '🤤', '🤧', '🥵', '😳',
  '😉', '😲', '😯', '🥳', '😈', '😺','😸', '😹', '😻', '😽', '😼', '👍', '✌️',
  '🤟', '🤘', '👌', ' 🤙', '🙌', '🙏', '👏', '🤞', ' 👀', '❤️', '🧡', '💛',
   '💚', '💙', '💜', '🤎', '🖤', '❣️', '💕', '💞', '💓', '💗', '💖', '💘',
   '💝', '💟', '♥️', '💔', '💌', '🎊', '🎉', '🔝', '🆒', '🆗',
   '💑', '👩‍❤️‍👩', '👨‍❤️‍👨', '💏', '👩‍❤️‍💋‍👩', '👨‍❤️‍💋‍👨', '👸', '🤴', '🙆‍♀️', '🙆‍♂️', '🕺', '💃', '🙈', '🐱', '🐶', '🔆', '🔅', '☀️','🎆', '🌅', '🌄', '🌠',
    '🎇', '🎆', '🌇', '🌌', '💡', '🏖', '🏝', '💯', '✅', '✔️', '☑️', '✓', '➕', '🎁', '💪', '👼',
     '🍀', '🌞', '🌸', '🌼', '🌻', '🌺', '🌹', '💐', '🌈', '🎈', '💥', '🔥', ':)',
      '👉👈', '🦋', '🐥', '🐾', '⭐', '🌟', '💫', '✨', '🐛', '💦', '👑',
      '🍑', '🍥', '🍺', '🍻', '🥂', '🍰', '🥇', '🎖', '🏅', '🧚‍♀️', '🧚', '🧚‍♂️', '🌤']


neg_emojis = ['🤨', '😐', '😑', '😶', '🙄', '😣', '😥', '🤐', '😫', '😓',
 '😔', '😕', '☹️', '🙁', '😖', '😞', '😟', '😤', '😢', '😭', '😦', '😧',
  '😨', '😩', '😬', '😰', '😡', '😠', '🤬', '🤥', '🤕', '🤢', '🤯', '🤮', '😪', '🤕', '👿', '😾',
   '😿', '🙀', '👎', '🤦‍♀️', '🤦‍♂️', '🙎‍♀️', '🙎‍♂️', '🙍‍♀️', '🙍‍♂️', '🙅‍♀️', '🙅‍♂️', '🥀', '🌥', '🌧',
    '⛈', '💔', '💢', '🔴', '🚨', '🧯', '⁉️', '🤡', '💩', '🆖', '☓', '❌', '☒']


neutral_emojis = ['😴', '🤒', '🤢', '😷', '😵', '🦠', '🥶', '🥴', '💤', '😱', '🤔']


def del_emoji(text_data):
    str_emo = emoji.demojize(text_data)
    text = re.sub(':.*?:', '', str_emo)
    return re.sub('\s+', ' ', text)


def replace_all_emoji(text_data):
    str_emo = emoji.demojize(text_data)
    text = re.sub(':.*?:', 'emoji', str_emo)
    return re.sub('\s+', ' ', text)


def replace_emoji_by_class(text_data):
    tokens = text_data.split()
    new_tokens = []
    for t in tokens:
        if t in pos_emojis:
            t = 'pos_emoji'
        elif t in neg_emojis:
            t = 'neg_emoji'
        else:
            t = re.sub(':.*?:', 'neutral_emoji', emoji.demojize(t))
        new_tokens.append(t)
    return " ".join(new_tokens)