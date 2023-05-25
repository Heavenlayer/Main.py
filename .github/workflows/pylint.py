
import telebot

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token
bot = telebot.TeleBot('5610358991:AAECfUJgo1DTiWMBwfrK48Q0XoIOGadHZXA')


@bot.message_handler(commands=['start'])
def send_welcome(message):
  try:
    bot.reply_to(
      message,
      "🎨 Welcome to our professional design services! How may we assist you today? 🤩\n\n"
      "To get started, please upload the high-resolution design you would like for your custom sticker or mobile skin. 🖼️\n\n"
      "Kindly note that the minimum resolution requirement is 1080p.")
  except Exception as e:
    print(f"An error occurred in 'send_welcome' function: {str(e)}")


@bot.message_handler(content_types=['photo'])
def process_photo(message):
  try:
    chat_id = message.chat.id
    photo = message.photo[
      -1]  # Assumes the last photo in the message is the highest resolution

    if photo.width < 1080 or photo.height < 1080:
      bot.reply_to(
        message,
        "⚠️ Oops! The resolution of the photo should be 1080p or higher. Please upload a higher quality image. 📸"
      )
    else:
      bot.send_message(
        chat_id,
        "🎉 Congratulations! Your request has been received and accepted. 🙌")
      bot.send_message(
        chat_id,
        "📥 We have successfully received the high-resolution design you uploaded. 🖼️"
      )
      bot.send_message(
        chat_id,
        "⏳ Our team of skilled professionals will now meticulously process your design to create a stunning custom sticker or mobile skin. 🛠️"
      )
      bot.send_message(
        chat_id,
        "💫 We appreciate your choice in selecting our premium services! You can expect to receive the buying link for your personalized product within the next 24 hours. 😊"
      )

      # Additional information gathering
      bot.send_message(
        chat_id,
        "📋 To provide you with the best results, we would like to gather some additional details about your design. Please answer the following questions:\n\n"
        "1️⃣ What is the desired size for your sticker or mobile skin? (e.g., 4x4 inches)\n\n"
        "2️⃣ Do you have any specific color preferences or design instructions?\n\n"
        "3️⃣ If you want to create a layer, please provide the model of your device."
      )

      bot.register_next_step_handler(message, process_additional_info)
  except Exception as e:
    print(f"An error occurred in 'process_photo' function: {str(e)}")


def process_additional_info(message):
  try:
    chat_id = message.chat.id

    # Process the additional information provided by the client
    size = message.text
    color_preferences = message.text
    device_model = message.text

    # Example: Send a confirmation message with the gathered information
    confirmation_message = f"📝 Thank you for providing the additional details. Here is a summary of your design preferences:\n\n" \
                           f"📏 Size: {size}\n" \
                           f"🎨 Color Preferences/Design Instructions: {color_preferences}\n" \
                           f"📱 Device Model (for layer): {device_model}\n\n" \
                           f"🛒 We will process your design accordingly. You will receive the buying link within the next 24 hours. Thank you!"
    bot.send_message(chat_id, confirmation_message)

    # Send the collected information to your registered Telegram account (replace 'YOUR_ACCOUNT_ID' with your account ID)
    collected_info_message = f"📩 New Design Request:\n\n" \
                             f"📏 Size: {size}\n" \
                             f"🎨 Color Preferences/Design Instructions: {color_preferences}\n" \
                             f"📱 Device Model (for layer): {device_model}\n\n" \
                             f"📸 Photo: {message.photo[-1].file_id}"
    bot.send_message('t.me/Heavencollect', collected_info_message)
  except Exception as e:
    print(f"An error occurred in 'process_additional_info' function: {str(e)}")


# Start the bot
try:
  bot.polling()
except Exception as e:
  print(f"An error occurred while polling the bot: {str(e)}")























