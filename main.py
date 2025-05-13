from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import urllib.request
import os
import subprocess
import time

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        button = Button(text='Скачать и установить', size_hint=(None, None), size=(200, 50))
        button.bind(on_press=self.download_and_install)
        layout.add_widget(button)
        return layout

    def download_and_install(self, instance):
        # Укажите ссылку на файл на GitHub
        file_url = "https://github.com/your-username/your-repo/raw/main/yourfile.apk"  # Замените на свою ссылку
        file_path = "/sdcard/Download/yourfile.apk"  # Путь, куда будет загружен файл

        # Скачиваем файл
        urllib.request.urlretrieve(file_url, file_path)

        # Устанавливаем файл
        self.install_apk(file_path)

    def install_apk(self, file_path):
        # Проверяем, существует ли файл
        if os.path.exists(file_path):
            # Команда для установки APK через ADB (предполагаем, что установлены нужные утилиты)
            command = f"adb install {file_path}"
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

            if process.returncode == 0:
                print("APK успешно установлен")
                time.sleep(2)
                # Запуск приложения после установки (если нужно)
                # Вставьте здесь код для запуска приложения, например, используя команду ADB
                package_name = "com.yourapp.package"  # Замените на имя пакета вашего приложения
                subprocess.Popen(f"adb shell monkey -p {package_name} -c android.intent.category.LAUNCHER 1", shell=True)
            else:
                print(f"Ошибка установки: {stderr}")
        else:
            print("Файл не найден")

if __name__ == '__main__':
    MainApp().run()
