import vk_api


def captcha_handler(captcha):


    key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()


    return captcha.try_again(key)


def main():

    login, password = 'Anton@vk.com', 'mypassword'
    vk_session = vk_api.VkApi(
        login, password,
        captcha_handler=captcha_handler  # функция для обработки капчи
    )

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return



if __name__ == '__main__':
    main()