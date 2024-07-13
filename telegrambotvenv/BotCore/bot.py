from telegram import   InlineKeyboardButton, Update, InlineKeyboardMarkup
from telegram.ext import  ApplicationBuilder, ConversationHandler,CommandHandler, ContextTypes



   
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    keyboard=[      
    ]
    row1=[
            InlineKeyboardButton("ВНЖ", callback_data="vnj"),
            InlineKeyboardButton("NIF", callback_data="nif"),
            InlineKeyboardButton("Банковские счета", callback_data="bank")            

    ]
    row2=[
            InlineKeyboardButton("Аренда жилья", callback_data="rent"),
            InlineKeyboardButton("Условия оказания услуг", callback_data="term")
    ]
    keyboard.append(row1)
    keyboard.append(row2)
    reply_markup=InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(f"""🇵🇹 Добро пожаловать в ваш персональный гид по релокации в Португалию! 🌞

ReloBot здесь, чтобы облегчить ваш переезд и сделать его как можно более гладким и беззаботным.

Услуги:
🔹 ВНЖ Португалии: Полное сопровождение и подготовка документов для всех типов вида на жительство.
🔹 Оформление налоговых номеров (NIF): Быстрая помощь в получении первого ключевого документа в Португалии.
🔹 Открытие банковского счета: Эффективное открытие подходящего банковского счета без дальнейших блокировок.
🔹 Контракт аренды: для визы, ВНЖ и других целей.
💬 Чтобы начать оформление услуг или узнать более подробную информацию, пожалуйста, выберите интересующую вас тему.
""", reply_markup=reply_markup)

async def gender_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Retrieve the value from the clicked button and take the next step."""
    result = update.callback_query.data
    query=update.callback_query
    if(result!=""):
       
       
        #await query.edit_message_text('You selectetd   ' + selected_button) 
        if result=='vnj':
            answer="""🇵🇹 Информация о ВНЖ в Португалии
            
            **ВНЖ D7 для людей с пассивным доходом:**
            ⌛ Время ожидания: 1-2 месяца после подачи документов
            🤑 Доход: пассивный регулярный доход от €820
            💸 Сбережения: не менее €9840

            **ВНЖ Digital Nomad для тех, кто работает удалённо:**
            ⌛ Время ожидания: 1-2 месяца после подачи документов
            🤑 Требования к доходу: €3280+ в месяц
            📄 Работа: удаленная работа или ИП с не-португальскими клиентами
            ✍ Контракт: начало 3+ месяца до подачи, длительность 1+ лет

            **ВНЖ 89.2в Португалии после открытия самозанятости или трудоустройства:**
            ✍ Подача: внутри Португалии
            🤑 Депозит: не обязателен, но нужен банковский счёт
            💸 Доход: минимальная месячная зарплата суммарно

            💼 Для получения дополнительной информации, записи на консультацию или в случае возникновения вопросов, пожалуйста, используйте опции ниже."""
            keyboardvnj=[
                [
                    InlineKeyboardButton("Написать эксперту", callback_data="contact_expert"),
                    InlineKeyboardButton("Заказать консультацию", callback_data="order_consultation"),
                ]
            ]
            reply_markupvnj=InlineKeyboardMarkup(keyboardvnj)
            ##await update.callback_query.message.edit_text(answer )
            await update.effective_chat.send_message(answer, reply_markup=reply_markupvnj)
        if result == 'nif':
            answer="""🇵🇹 Информация о получении NIF (Налоговый Номер)
            **Процесс получения NIF:**
            ⌛ Сроки: 3-4 дня
            📋 Требуемые документы: паспорт и подтверждение адреса (выписка с банковского счета)
            🏢 Процесс: сделаем удаленно, с запросом кодов доступа от личного кабинета финаншас.

            💼 Для получения дополнительной информации, получения NIF или в случае возникновения вопросов, пожалуйста, используйте опции ниже."""
            keyboardnif=[
                [
                    InlineKeyboardButton("Написать эксперту", callback_data="contact_expert"),
                    InlineKeyboardButton("Заказать NIF", callback_data="order_nif"),
                ]
            ]
            reply_markupvnj=InlineKeyboardMarkup(keyboardnif)
            ##await update.callback_query.message.edit_text(answer )
            await update.effective_chat.send_message(answer, reply_markup=reply_markupvnj)
        if result == "bank":
            answer="""🇵🇹 Информация об открытии банковских счетов в Португалии
            **Процесс открытия банковского счета:**
            ⌛ Сроки оформления: 10-15 рабочих дней
            📋 Требуемые документы: действующий паспорт, контракт аренды в Португалии, NIF (налоговый номер), подтверждение источников дохода.

            💼 Для получения дополнительной информации, помощи в выборе банка или в случае возникновения вопросов, пожалуйста, используйте опции ниже.

            Обратите внимание: Банк может запросить дополнительную сопутствующую информацию в зависимости от вашей ситуации."""
            keyboardbank=[
                [
                    InlineKeyboardButton("Написать эксперту", callback_data="contact_expert"),
                    InlineKeyboardButton("Получить помощь в выборе банка", callback_data="help_bank_choice"),
                ]
            ]
            reply_markupvnj=InlineKeyboardMarkup(keyboardbank)
            ##await update.callback_query.message.edit_text(answer )
            await update.effective_chat.send_message(answer, reply_markup=reply_markupvnj)
        if result == "rent":
            answer="""🇵🇹 Контракт аренды жилья в Португалии

            Мы помогаем в оформлении реального адреса в Португалии с договором и регистрацией, необходимыми для различных бюрократических процедур, включая:
            🏦 Открытие банковского счёта
            📑 Подача документов на визу или ВНЖ
            💼 Смена налогового адреса 

            💬 Для получения дополнительной информации или помощи в аренде жилья, пожалуйста, используйте опции ниже."""
            keyboardrent=[
                [
                    InlineKeyboardButton("Написать эксперту", callback_data="contact_expert"),
                    InlineKeyboardButton("Получить помощь в аренде жилья", callback_data="help_find_housing"),
                ]
            ]
            reply_markupvnj=InlineKeyboardMarkup(keyboardrent)
            ##await update.callback_query.message.edit_text(answer )
            await update.effective_chat.send_message(answer, reply_markup=reply_markupvnj)
        if result == "term":
            answer="""Стоимость услуг:

            🔹 ВНЖ: от 2000€ до 4500€
            🔹 NIF: 250€
            🔹 Банковские счета: 1000€ с личным визитом, 3000€ полностью удаленно
            🔹 Контракт аренды: 1500-2500€


            Цены могут варьироваться в зависимости от конкретных требований и условий.

            Чтобы заказать услугу, пожалуйста, нажмите на кнопку ниже."""
            keyboardterm=[
                [
                    InlineKeyboardButton("Заказать услугу", callback_data="order_service"),
                ]
            ]
            reply_markupvnj=InlineKeyboardMarkup(keyboardterm)
            ##await update.callback_query.message.edit_text(answer )
            await update.effective_chat.send_message(answer, reply_markup=reply_markupvnj)
        if result == "contact_expert":
            answer="""📞 **Свяжитесь с нашим экспертом:**

            📱 Telegram @antoniosip
            💬 WhatsApp: +7 911 184 28 16
            🔗 [Instagram](https://instagram.com/goresident)
            Мы готовы ответить на ваши вопросы и помочь с релокацией в Португалию!"""
            
            await update.effective_chat.send_message(answer)

        elif result == "order_nif":
            answer="""🇵🇹 **Заказ NIF**

            Для заказа NIF, пожалуйста, следуйте следующим шагам:
            1. Подготовьте необходимые документы: паспорт или удостоверение личности и адрес проживания.
            2. Свяжитесь с нами через Telegram или WhatsApp для дальнейших инструкций.
            📱 Telegram @antoniosip
            💬 WhatsApp: +79111842816
            Мы поможем вам с оформлением NIF быстро и эффективно!"""
            
            await update.effective_chat.send_message(answer)

        elif result == "help_bank_choice":
            answer="""🇵🇹 **Помощь в выборе банка**

            Для получения помощи в выборе банка и уточнения деталей открытия счета, пожалуйста, свяжитесь с нами:
            📱 Telegram @botusername
            💬 WhatsApp: +1234567890
            Мы поможем вам выбрать наиболее подходящий банк и пройти процесс открытия счета!"""

            await update.effective_chat.send_message(answer)
        elif result == "help_find_housing":
            answer="""🇵🇹 **Помощь в аренде жилья**
            
            Для получения помощи в аренде жилья и оформлении необходимых документов, пожалуйста, свяжитесь с нами:
            📱 Telegram @botusername
            💬 WhatsApp: +1234567890
        
            Мы поможем вам найти подходящее жильё и оформить все необходимые документы!"""
            
            await update.effective_chat.send_message(answer)
        elif result == "order_consultation":
            answer="""Для заказа консультации, пожалуйста, свяжитесь с нами через удобный вам канал связи."""
            
            await update.effective_chat.send_message(answer)
    else:
        result= update.message.text
     
       


   # await update..caption(selected_button)


