from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardMarkup, KeyboardButton

# for menu
button = KeyboardButton('/menu')
orientation = InlineKeyboardButton('Расписание', callback_data='orientation')
canteen = InlineKeyboardButton('Столовая', callback_data='canteen')
additionally = InlineKeyboardButton('Дополнительно', callback_data='additionally')
help_text = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
help_text.add(button)

# for how_class
class5 = InlineKeyboardButton('𝟝', callback_data='5')
class6 = InlineKeyboardButton('𝟞', callback_data='6')
class7 = InlineKeyboardButton('𝟟', callback_data='7')
class8 = InlineKeyboardButton('𝟠', callback_data='8')
class9 = InlineKeyboardButton('𝟡', callback_data='9')
class10 = InlineKeyboardButton('𝟙𝟘', callback_data='10')
class11 = InlineKeyboardButton('𝟙𝟙', callback_data='11')

# for how_letter
letter_a = InlineKeyboardButton('а', callback_data='a')
letter_b = InlineKeyboardButton('б', callback_data='b')

# for fast_orientation InlineKeyboardMarkup.
breakfast = InlineKeyboardButton('Завтрак', callback_data='breakfast')
lunch = InlineKeyboardButton('Обед', callback_data='lunch')
afternoon_tea = InlineKeyboardButton('Полдник', callback_data='afternoon_tea')
dinner = InlineKeyboardButton('Ужин', callback_data='dinner')
sonnik = InlineKeyboardButton('Сонник', callback_data='sonnik')

# for menu_2
teachers = InlineKeyboardButton("Учителя", callback_data='teachers')
director = InlineKeyboardButton("Директор", callback_data='director')
head_teachers = InlineKeyboardButton("Завучи", callback_data='head_teachers')
boarding_school = InlineKeyboardButton("Интернат", callback_data='boarding_school')

# for orientation 3
educators = InlineKeyboardButton("Воспитательницы", callback_data='educators')
cleaning_day = InlineKeyboardButton("День уборки", callback_data='cleaning_day')
modes = InlineKeyboardButton("Режимы", callback_data='modes')
cancel = InlineKeyboardButton("Назад", callback_data='cancel')

orientation1 = InlineKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True).add(orientation,
                                                                canteen).add(additionally)
fast_orientation = InlineKeyboardMarkup(one_time_keyboard=True).add(breakfast, lunch, afternoon_tea).add(
    dinner, sonnik)

how_class = InlineKeyboardMarkup(one_time_keyboard=True).add(class5, class6, class7, class8, class9, class10, class11)

how_letter = InlineKeyboardMarkup(one_time_keyboard=True).add(letter_a, letter_b)

menu_2 = InlineKeyboardMarkup().add(teachers, head_teachers, director).add(boarding_school)

orientation3 = InlineKeyboardMarkup().add(educators).add(cleaning_day, modes).add(cancel)
