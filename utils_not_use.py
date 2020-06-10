

def first_family(cnt1=10, cnt2=10, cnt3=3, cnt4=3, cnt5=3):
    print('Starting First Family')
    go_home()

    wait_click('enter_battle.jpg')
    wait_click('epic_quest.jpg')
    wait_click('first_family.jpg')

    def first_falimy_iter(but1, but2, but3, cnt):
        wait_click(but1)  # 사이좋은 형제
        wait_click(but2)  # 사이좋은 형제
        # sleep_click_v2(1274, 730, 1454, 784, 1.01, 2.23)  # 때려 부술 시간_4
        if but3 is not None:
            check_click_in('battle.jpg', pag.locateOnScreen(os.path.join(button_path2, but3)))
            time.sleep(random.uniform(1, 1.5))
        else:
            pass
        iter_battle(cnt)
        time.sleep(random.uniform(2.71, 3.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))

    if cnt1 > 0:
        first_falimy_iter('first_family_01.jpg', 'first_family_01_01.jpg', 'first_family_01_01_04.jpg', cnt1)
        # wait_click('first_family_01.jpg')  # 사이좋은 형제
        # wait_click('first_family_01_01.jpg')  # 사이좋은 형제
        # sleep_click_v2(1274, 730, 1454, 784, 1.01, 2.23)  # 때려 부술 시간_4
        # iter_battle(cnt1)
        #
        # time.sleep(random.uniform(2.71, 3.53))
        # check_click('back_button.jpg')
        # time.sleep(random.uniform(0.71, 1.53))
        # check_click('back_button.jpg')
        # time.sleep(random.uniform(0.71, 1.53))

    if cnt2 > 0:
        first_falimy_iter('first_family_01.jpg', 'first_family_01_02.jpg', 'first_family_01_02_04.jpg', cnt2)

    if cnt3 > 0:
        wait_click('first_family_02.jpg')  # 뉴 페이스
        wait_click('first_family_02_01.jpg')  # 인휴먼 공주
        iter_battle(cnt3)

        # time.sleep(random.uniform(2.71, 3.53))
        # wait_click('ok_button.jpg')
        # time.sleep(random.uniform(0.71, 1.53))
        # check_click('reload_button.jpg')
        time.sleep(random.uniform(2.71, 3.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))

    if cnt4 > 0:
        wait_click('first_family_02.jpg')  # 뉴 페이스
        wait_click('first_family_02_02.jpg')  # 사나운 초록색
        iter_battle(cnt4)
        # time.sleep(random.uniform(3.71, 4.53))
        # check_click('ok_button.jpg')
        # time.sleep(random.uniform(0.71, 1.53))
        # check_click('reload_button.jpg')
        time.sleep(random.uniform(2.71, 3.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))

    if cnt5 > 0:
        wait_click('first_family_03.jpg')  # 뉴 페이스
        wait_click('first_family_03_01.jpg')  # 라트베리아
        iter_battle(cnt5)
        # time.sleep(random.uniform(3.71, 4.53))
        # check_click('ok_button.jpg')
        # time.sleep(random.uniform(0.71, 1.53))
        # check_click('reload_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))
    time.sleep(random.uniform(2.71, 3.53))
    print('end first_family')


def x_force(cnt1=10, cnt2=10, cnt3=3, cnt4=3, cnt5=3):
    print('Starting X Force')
    go_home()

    wait_click('enter_battle.jpg')
    wait_click('epic_quest.jpg')

    wait_click('x_force.jpg')

    def x_force_iter(but1, but2, but3, cnt):
        wait_click(but1)  # 엉망인 친구들
        wait_click(but2)  # 이런 세상에

        # sleep_click_v2(1274, 730, 1454, 784, 1.01, 2.23)  # 이런 세상에 #4
        if but3 is not None:
            check_click_in('battle.jpg', pag.locateOnScreen(os.path.join(button_path2, but3)))
        else:
            pass
        iter_battle(cnt)
        time.sleep(random.uniform(2.71, 3.53))

        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))

    if cnt1 > 0:
        x_force_iter('x_force_01.jpg', 'x_force_01_01.jpg', 'x_force_01_01_04.jpg', cnt1)
        # wait_click('x_force_01.jpg')  # 엉망인 친구들
        # wait_click('x_force_01_01.jpg')  # 이런 세상에
        #
        # sleep_click_v2(1274, 730, 1454, 784, 1.01, 2.23)  # 이런 세상에 #4
        #
        # iter_battle(cnt1)
        # time.sleep(random.uniform(2.71, 3.53))
        #
        # check_click('back_button.jpg')
        # time.sleep(random.uniform(0.71, 1.53))
        # check_click('back_button.jpg')
        # time.sleep(random.uniform(0.71, 1.53))

    if cnt2 > 0:
        x_force_iter('x_force_01.jpg', 'x_force_01_02.jpg', 'x_force_01_02_04.jpg', cnt2)

    if cnt3 > 0:
        x_force_iter('x_force_02.jpg', 'x_force_02_01.jpg', None, cnt3)
        # wait_click('x_force_02.jpg')  # 머저리
        # wait_click('x_force_02_01.jpg')  # 크롬 덩어리
        # iter_battle(cnt3)
        # time.sleep(random.uniform(2.71, 3.53))
        # check_click('back_button.jpg')
        # time.sleep(random.uniform(0.71, 1.53))
        # check_click('back_button.jpg')
        # time.sleep(random.uniform(0.71, 1.53))

    if cnt4 > 0:
        x_force_iter('x_force_02.jpg', 'x_force_02_02.jpg', None, cnt4)
        # wait_click('x_force_02.jpg')  # 머저리
        # wait_click('x_force_02_02.jpg')  # 사이 로그 아웃
        # iter_battle(cnt4)
        # time.sleep(random.uniform(2.71, 3.53))
        # check_click('back_button.jpg')
        # time.sleep(random.uniform(0.71, 1.53))
    if cnt5 > 0:    # 케이블 자르기
        x_force_iter('x_force_03.jpg', 'x_force_03_01.jpg', None, cnt5)

    time.sleep(random.uniform(2.71, 3.53))
    print('end x_force')


def rise_xman(cnt1=10, cnt2=10, cnt3=10, cnt4=10, cnt5=2, cnt6=2):
    print('Starting Rise X man')
    go_home()

    wait_click('enter_battle.jpg')
    wait_click('epic_quest.jpg')
    wait_click('rise_xman.jpg')    # select_mission
    # sleep_click_v2(1221, 215, 1712, 800, 1.01, 1.53)  # select_mission

    if cnt1 > 0:
        wait_click('rise_xman_01.jpg')  # chasing
        # sleep_click_v2(767, 764, 860, 854, 1.01, 1.53)  # chasing
        time.sleep(random.uniform(1.01, 1.53))
        wait_click('rise_xman_01_01.jpg')
        # sleep_click_v2(308, 315, 545, 674, 1.01, 2.23)  # 악당이되다
        # sleep_click_v2(1274, 730, 1454, 784, 1.01, 2.23)  # select_battle
        check_click_in('battle.jpg', pag.locateOnScreen(os.path.join(button_path2, 'rise_xman_01_01_04.jpg')))
        iter_battle(cnt1)
        time.sleep(random.uniform(2.71, 3.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(1.71, 2.53))
        check_click('back_button.jpg')

    if cnt2 > 0:
        wait_click('rise_xman_01.jpg')  # chasing
        # sleep_click_v2(767, 764, 860, 854, 1.01, 1.53)  # chasing
        time.sleep(random.uniform(1.01, 1.53))
        wait_click('rise_xman_01_02.jpg')
        # sleep_click_v2(646, 317, 879, 676, 1.01, 2.23)  # 친구와 적
        # sleep_click_v2(1274, 730, 1454, 784, 1.01, 2.23)  # select_battle
        check_click_in('battle.jpg', pag.locateOnScreen(os.path.join(button_path2, 'rise_xman_01_02_04.jpg')))
        iter_battle(cnt2)
        time.sleep(random.uniform(2.71, 3.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(1.71, 2.53))
        check_click('back_button.jpg')
    else:
        pass

    if cnt3 > 0:
        wait_click('rise_xman_01.jpg')  # chasing
        # sleep_click_v2(767, 764, 860, 854, 1.01, 1.53)  # chasing
        time.sleep(random.uniform(1.01, 1.53))
        wait_click('rise_xman_01_03.jpg')
        # sleep_click_v2(977, 314, 1220, 675, 1.01, 2.23)  # 몰아치는 폭풍
        # sleep_click_v2(1274, 730, 1454, 784, 1.01, 2.23)  # select_battle
        check_click_in('battle.jpg', pag.locateOnScreen(os.path.join(button_path2, 'rise_xman_01_03_04.jpg')))
        iter_battle(cnt3)
        time.sleep(random.uniform(2.71, 3.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(1.71, 2.53))
        check_click('back_button.jpg')
    else:
        pass

    if cnt4 > 0:
        wait_click('rise_xman_01.jpg')  # chasing
        # sleep_click_v2(767, 764, 860, 854, 1.01, 1.53)  # chasing
        time.sleep(random.uniform(1.01, 1.53))
        wait_click('rise_xman_01_04.jpg')
        # sleep_click_v2(1312, 311, 1551, 670, 2.01, 3.23)  # 맹목적 전투
        # sleep_click_v2(1274, 730, 1454, 784, 2.01, 3.23)  # select_battle
        iter_battle(cnt4)
        time.sleep(random.uniform(2.71, 3.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(1.71, 2.53))
        check_click('back_button.jpg')
        # time.sleep(random.uniform(1.71, 2.53))
        # check_click('back_button.jpg')
    else:
        pass

    if cnt5 > 0:
        wait_click('rise_xman_02.jpg')
        wait_click('rise_xman_02_01.jpg')
        # sleep_click_v2(1312, 311, 1551, 670, 2.01, 3.23)  # 매그니토의 힘
        # sleep_click_v2(1274, 730, 1454, 784, 2.01, 3.23)  # select_battle
        iter_battle(cnt5)
        time.sleep(random.uniform(2.71, 3.53))
        check_click('ok_button.jpg')
        time.sleep(random.uniform(1.71, 2.53))
        check_click('reload_button.jpg')
        time.sleep(random.uniform(1.71, 2.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(1.71, 2.53))
        # time.sleep(random.uniform(1.71, 2.53))
        # check_click('back_button.jpg')
    else:
        pass

    if cnt6 > 0:
        # wait_click('rise_xman_02.jpg')
        wait_click('rise_xman_02_02.jpg')
        # sleep_click_v2(1312, 311, 1551, 670, 2.01, 3.23)  # 되살아난 피닉스
        # sleep_click_v2(1274, 730, 1454, 784, 2.01, 3.23)  # select_battle
        iter_battle(cnt6)
        time.sleep(random.uniform(2.71, 3.53))
        check_click('ok_button.jpg')
        time.sleep(random.uniform(1.71, 2.53))
        check_click('reload_button.jpg')
        time.sleep(random.uniform(1.71, 2.53))
    else:
        pass
    time.sleep(random.uniform(2.71, 3.53))
    print('end rise_xman')

    # time.sleep(random.uniform(0.71, 1.53))
    # wait_click('back_button.jpg')


def sorcerer_supreme(cnt1=3, cnt2=3):
    print('Starting Sorcerer Supreme')
    go_home()

    wait_click('enter_battle.jpg')
    wait_click('epic_quest.jpg')
    # time.sleep(random.uniform(0.71, 1.53))
    wait_click('sorcerer_supreme.jpg')
    # time.sleep(random.uniform(0.71, 1.53))

    if True:
        wait_click('sorcerer_supreme_01.jpg')  # 회상 임무
        time.sleep(random.uniform(0.71, 1.53))
        # wait_click('sorcerer_supreme_01_01.jpg')  # 수도원으로 가는 길
        # wait_click('sorcerer_supreme_01_02.jpg')  # 의문의 습격자
        # wait_click('sorcerer_supreme_01_03.jpg')  # 위기의 수도원
        wait_click('sorcerer_supreme_01_04.jpg')  # 어둠의 힘
        time.sleep(random.uniform(0.71, 1.53))

        drag_from = pag.locateOnScreen(os.path.join('buttons(960x540)/', 'sorcerer_supreme_01_04_04.jpg'),
                                       grayscale=True, confidence=.99)
        drag_to = pag.locateOnScreen(os.path.join('buttons(960x540)/', 'sorcerer_supreme_01_04_01.jpg'),
                                     grayscale=True, confidence=.99)
        pag.moveTo(random.uniform(drag_from[0], drag_from[0]+drag_from[2]*0.5),
                   random.uniform(drag_from[1], drag_from[1]+drag_from[3]))
        pag.dragTo(random.uniform(drag_to[0], drag_to[0]+drag_to[2]*0.5),
                   random.uniform(drag_to[1], drag_to[1]+drag_to[3]),
                   random.uniform(0.7, 1.2), button='left')
        # # x, 665, y: 245
        # # x, 1251, y: 783
        # pag.moveTo(random.uniform(851, 1024), random.uniform(673, 752))
        # pag.dragTo(random.uniform(851, 1024), random.uniform(302, 346),
        #            random.uniform(0.4, 1.2), button='left')
        # x, 1272, y: 692
        # x, 1462, y: 751
        # sleep_click_v2(1272, 692, 1462, 751, 1.01, 2.23)  # 어둠의 힘 #6
        time.sleep(random.uniform(1.71, 2.53))
        check_click_in('battle.jpg',
                       pag.locateOnScreen(os.path.join(button_path2, 'sorcerer_supreme_01_04_06.jpg')))

        iter_battle(cnt1)
        time.sleep(random.uniform(3.71, 4.53))

        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))
        check_click('back_button.jpg')
        time.sleep(random.uniform(0.71, 1.53))

    if cnt2 > 0:
        check_click_v2('sorcerer_supreme_02.jpg')
        time.sleep(random.uniform(1.71, 2.53))
        # if pag.locateOnScreen(os.path.join(button_path2, 'sorcerer_supreme_02_02_locked.jpg'), grayscale=True, confidence=.9):
        #     check_click_v2('sorcerer_supreme_02_01.jpg')  # 회상 임무
        # elif pag.locateOnScreen(os.path.join(button_path2, 'sorcerer_supreme_02_02.jpg'), grayscale=True, confidence=.9):
        #     check_click_v2('sorcerer_supreme_02_02.jpg')  # 회상 임무
        if pag.locateOnScreen(os.path.join(button_path2, 'sorcerer_supreme_02_02.jpg'), grayscale=True, confidence=.9):
            check_click_v2('sorcerer_supreme_02_02.jpg')  # 회상 임무
        else:
            check_click_v2('sorcerer_supreme_02_01.jpg')  # 회상 임무
        time.sleep(random.uniform(3.71, 4.53))
        iter_battle(cnt2)
        time.sleep(random.uniform(3.71, 4.53))
    else:
        pass
    time.sleep(random.uniform(2.71, 3.53))
    print('end sorcerer_supreme')


def rise_xman_all_account():
    change_account(3)
    time.sleep(random.uniform(2.71, 3.53))
    rise_xman(10, 10, 10, 10, 2, 2)     # 10, 10, 10, 10, 2, 2
    time.sleep(random.uniform(2.71, 3.53))

    change_account(1)  # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
    time.sleep(random.uniform(2.71, 3.53))
    rise_xman(10, 10, 10, 10, 2, 2)     # 10, 10, 10, 10, 2, 2
    time.sleep(random.uniform(2.71, 3.53))

    change_account(2)
    time.sleep(random.uniform(2.71, 3.53))
    rise_xman(10, 10, 10, 10, 2, 2)     #
    time.sleep(random.uniform(2.71, 3.53))


def first_family_all_account():
    change_account(3)
    time.sleep(random.uniform(2.71, 3.53))
    first_family(10, 10, 3, 3, 3)
    time.sleep(random.uniform(2.71, 3.53))

    change_account(2)
    time.sleep(random.uniform(2.71, 3.53))
    first_family(10, 10, 3, 3, 3)
    time.sleep(random.uniform(2.71, 3.53))

    change_account(1)  # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
    time.sleep(random.uniform(2.71, 3.53))
    first_family(10, 0, 3, 3, 3)
    time.sleep(random.uniform(2.71, 3.53))


def x_force_all_account():
    change_account(1)  # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
    time.sleep(random.uniform(2.71, 3.53))
    x_force(10, 10, 3, 3, 3)       # 10, 10, 3, 3, 3
    time.sleep(random.uniform(2.71, 3.53))

    change_account(2)
    time.sleep(random.uniform(2.71, 3.53))
    x_force(10, 10, 3, 3, 0)         # 10, 10, 3, 3, 0,  도미노 할 수 있는지 확인
    time.sleep(random.uniform(2.71, 3.53))

    change_account(3)
    time.sleep(random.uniform(2.71, 3.53))
    x_force(10, 0, 3, 0, 0)             # 10, 0, 3, 0, 0
    time.sleep(random.uniform(2.71, 3.53))


def sorcerer_supreme_all_account():
    # change_account(2)
    # time.sleep(random.uniform(2.71, 3.53))
    # sorcerer_supreme(3, 3)
    # time.sleep(random.uniform(2.71, 3.53))

    change_account(1)  # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
    time.sleep(random.uniform(2.71, 3.53))
    sorcerer_supreme(1, 3)
    time.sleep(random.uniform(2.71, 3.53))

    change_account(3)
    time.sleep(random.uniform(2.71, 3.53))
    sorcerer_supreme(3, 3)
    time.sleep(random.uniform(2.71, 3.53))


def dimension_mission_all_account():
    change_account(1)  # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
    time.sleep(random.uniform(2.71, 3.53))
    dimension_mission(10)
    time.sleep(random.uniform(2.71, 3.53))

    change_account(2)
    time.sleep(random.uniform(2.71, 3.53))
    dimension_mission(10)
    time.sleep(random.uniform(2.71, 3.53))

    change_account(3)
    time.sleep(random.uniform(2.71, 3.53))
    dimension_mission(10)
    time.sleep(random.uniform(2.71, 3.53))


def legendary_all_account():
    change_account(1)
    time.sleep(random.uniform(2.71, 3.53))
    legendary_battle(1)     # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
    time.sleep(random.uniform(2.71, 3.53))

    change_account(2)
    time.sleep(random.uniform(2.71, 3.53))
    legendary_battle(2)  # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
    time.sleep(random.uniform(2.71, 3.53))

    change_account(3)
    time.sleep(random.uniform(2.71, 3.53))
    legendary_battle(3)  # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
    time.sleep(random.uniform(2.71, 3.53))


def dim_to_epic_1(account, game_log):
    if check_exist('launch_game.jpg'):
        print('game start')
        check_click_v2('launch_game.jpg', 0.01, 0.11)
        time.sleep(60)

    go_home()
    if account is not None:
        change_account_v2(account)  # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
    else:
        account = check_current_account()
        print('current account ', account, ' is identified.')

    import threading
    time.sleep(random.uniform(2.71, 3.53))
    interupt_thread = threading.Thread(target=pass_interupt, name='pass_interupt', daemon=True)
    # interupt_thread.daemon = True
    interupt_thread.start()

    dim_to_do = game_log[str(account)]['dimension_mission'] - game_log[str(account)+'_do']['dimension_mission']
    if dim_to_do > 0:
        game_log[str(account)+'_do']['dimension_mission'] = dimension_mission(dim_to_do)
        print('Done : ', game_log[str(account)+'_do']['dimension_mission'])
        write_log(game_log)
        time.sleep(random.uniform(2.71, 3.53))

    first_family_v2(account, game_log)        # 10, 10, 3, 3, 3
    time.sleep(random.uniform(2.71, 3.53))
    # interupt_thread.join()


def dim_to_epic_2(account, game_log):
    if check_exist('launch_game.jpg'):
        print('game start')
        check_click_v2('launch_game.jpg', 0.01, 0.11)
        time.sleep(60)

    go_home()
    if account is not None:
        change_account_v2(account)  # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
    else:
        account = check_current_account()
        print('current account ', account, ' is identified.')

    x_force_v2(account, game_log)       # 10, 10, 3, 3, 3
    time.sleep(random.uniform(2.71, 3.53))

    log = sorcerer_supreme_v2(account, game_log)
    time.sleep(random.uniform(2.71, 3.53))
    write_log(log)
    time.sleep(random.uniform(2.71, 3.53))


def dim_to_epic_3(account, game_log):
    if check_exist('launch_game.jpg'):
        print('game start')
        check_click_v2('launch_game.jpg', 0.01, 0.11)
        time.sleep(60)

    go_home()
    if account is not None:
        change_account_v2(account)  # 1: 한또르(7602), 2: Stranghee, 3: ScOrpiOn2020
    else:
        account = check_current_account()
        print('current account ', account, ' is identified.')

    rise_xman_v2(account, game_log)     # 10, 10, 10, 10, 2, 2
    time.sleep(random.uniform(2.71, 3.53))


# dim_to_epic_1(account=2, game_log=game_log)
# dim_to_epic_1(account=1, game_log=game_log)
# dim_to_epic_1(account=3, game_log=game_log)

# dim_to_epic_2(account=1, game_log=game_log)
# dim_to_epic_2(account=2, game_log=game_log)
# dim_to_epic_2(account=3, game_log=game_log)

# dim_to_epic_3(account=1, game_log=game_log)
# dim_to_epic_3(account=2, game_log=game_log)
# dim_to_epic_3(account=3, game_log=game_log)

# detect_energy()

# def ocr_att_button():
#     # att5
#     # 1291, 920, 50, 50
#
#     screen = pag.screenshot(region=(1291, 920, 50, 50))
#     screen.save("att_button_tmp.jpg")
#     image = cv2.imread("att_button_tmp.jpg")
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     # gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
#     gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#     gray = cv2.medianBlur(gray, 1)
#     # rot = rotate(img, -20, reshape=False)
#     gray = rotate(gray, 20, reshape=False)
#     cv2.imwrite("att_button_tmp.jpg", gray)
#     custom_oem_psm_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789.%'
#     text = pytesseract.image_to_string(Image.open('att_button_tmp.jpg'), lang='eng',
#                                        # config='--psm 7 -c tessedit_char_whitelist=0123456789.%')
#                                        config=custom_oem_psm_config)
#     print(text)
#     # 숫자 인식률이 개그지, 파일 저장이 중간에 과다하게 들어가고, 파일 저장 없이 바로 이용하는 방법 아직 찾지 못함
#
#
# while True:
#     time.sleep(1)
#     ocr_att_button()

# att_1_x, att_1_y = x, 1502, y: 590
# 1502, 590, 140, 140
# att_button_1.jpg

# att_2_x, att_2_y = x, 1391, y: 711
# att_button_2.jpg

# att_3_x, att_3_y = x, 1666, y: 595
# att_4_x, att_4_y = x, 1414, y: 873
# att_5_x, att_5_y = x, 1246, y: 873
# 반지름은 140 정도 되는듯


"""
# Practice
# print('time.time(): ', time.time())     # 1584853046.2530923
# print('time.gmtime(time.time()): ', time.gmtime(time.time()))
# # time.struct_time(tm_year=2020, tm_mon=3, tm_mday=22,
# #                  tm_hour=4, tm_min=57, tm_sec=51, tm_wday=6, tm_yday=82, tm_isdst=0)
# print('time.gmtime(time.time()).tm_mday: ', time.gmtime(time.time()).tm_mday)   # 22


print("os.path.getctime('game_log.pickle'): ", os.path.getctime('game_log.pickle'))  # 1584806998.310804
last_modified = os.path.getctime('game_log.pickle')
print('time.gmtime(last_modified): ', time.gmtime(last_modified))
# time.struct_time(tm_year=2020, tm_mon=3, tm_mday=21,
#                  tm_hour=16, tm_min=9, tm_sec=58, tm_wday=5, tm_yday=81, tm_isdst=0)
print('time.gmtime(last_modified).tm_mday: ', time.gmtime(last_modified).tm_mday)   # 21

# load_log()
if os.path.exists('game_log.pickle'):
    now = time.strftime('%d', time.gmtime(time.time()))
    # time.time() : Return the time in seconds since the epoch as a floating point number.
    # the epoch is January 1, 1970, 00:00:00 (UTC) = gmtime(0)
    print("time.strftime('%d', time.gmtime(time.time())): ", now)
    # now = time.strftime('%d', time.time())
    # print("time.strftime('%d', time.time()): ", now)  # TypeError: Tuple or struct_time argument required
    wtime = time.strftime('%d', os.path.getctime('game_log.pickle'))
    # wtime = os.path.getctime('game_log.pickle')
    print(time.ctime(wtime), now)
    game_log = pickle.load(open('game_log.pickle', 'rb'))
    # print(game_log['max'], '\n', game_log[1])
else:
    init_log = {'max': {'dimension_mission': 10,
                        'first_family_01': 10, 'first_family_02': 10, 'first_family_03': 3, 'first_family_04': 3,
                        'first_family_05': 3, 'first_family_06': 3,
                        'x_force_01': 10, 'x_force_02': 10, 'x_force_03': 3, 'x_force_04': 3,
                        'x_force_05': 3, 'x_force_06': 3,
                        'rise_xman_01': 10, 'rise_xman_02': 10, 'rise_xman_03': 10, 'rise_xman_04': 10,
                        'rise_xman_05': 2, 'rise_xman_06': 2},
                1: {'dimension_mission': 10,
                    'first_family_01': 10, 'first_family_02': 10, 'first_family_03': 3, 'first_family_04': 3,
                    'first_family_05': 3, 'first_family_06': 0,
                    'x_force_01': 10, 'x_force_02': 10, 'x_force_03': 3, 'x_force_04': 3,
                    'x_force_05': 3, 'x_force_06': 0,
                    'rise_xman_01': 10, 'rise_xman_02': 10, 'rise_xman_03': 10, 'rise_xman_04': 10,
                    'rise_xman_05': 2, 'rise_xman_06': 2},
                2: {'dimension_mission': 10,
                    'first_family_01': 10, 'first_family_02': 10, 'first_family_03': 3, 'first_family_04': 3,
                    'first_family_05': 3, 'first_family_06': 0,
                    'x_force_01': 10, 'x_force_02': 10, 'x_force_03': 3, 'x_force_04': 3,
                    'x_force_05': 0, 'x_force_06': 0,
                    'rise_xman_01': 10, 'rise_xman_02': 10, 'rise_xman_03': 10, 'rise_xman_04': 10,
                    'rise_xman_05': 2, 'rise_xman_06': 2},
                3: {'dimension_mission': 10,
                    'first_family_01': 10, 'first_family_02': 0, 'first_family_03': 3, 'first_family_04': 3,
                    'first_family_05': 0, 'first_family_06': 0,
                    'x_force_01': 10, 'x_force_02': 0, 'x_force_03': 3, 'x_force_04': 3,
                    'x_force_05': 0, 'x_force_06': 0,
                    'rise_xman_01': 10, 'rise_xman_02': 10, 'rise_xman_03': 10, 'rise_xman_04': 10,
                    'rise_xman_05': 2, 'rise_xman_06': 2},
                '1_do': {'dimension_mission': 0,
                         'first_family_01': 0, 'first_family_02': 0, 'first_family_03': 0, 'first_family_04': 0,
                         'first_family_05': 0, 'first_family_06': 0,
                         'x_force_01': 0, 'x_force_02': 0, 'x_force_03': 0, 'x_force_04': 0,
                         'x_force_05': 0, 'x_force_06': 0,
                         'rise_xman_01': 0, 'rise_xman_02': 0, 'rise_xman_03': 0, 'rise_xman_04': 0,
                         'rise_xman_05': 0, 'rise_xman_06': 0},
                '2_do': {'dimension_mission': 0,
                         'first_family_01': 0, 'first_family_02': 0, 'first_family_03': 0, 'first_family_04': 0,
                         'first_family_05': 0, 'first_family_06': 0,
                         'x_force_01': 0, 'x_force_02': 0, 'x_force_03': 0, 'x_force_04': 0,
                         'x_force_05': 0, 'x_force_06': 0,
                         'rise_xman_01': 0, 'rise_xman_02': 0, 'rise_xman_03': 0, 'rise_xman_04': 0,
                         'rise_xman_05': 0, 'rise_xman_06': 0},
                '3_do': {'dimension_mission': 0,
                         'first_family_01': 0, 'first_family_02': 0, 'first_family_03': 0, 'first_family_04': 0,
                         'first_family_05': 0, 'first_family_06': 0,
                         'x_force_01': 0, 'x_force_02': 0, 'x_force_03': 0, 'x_force_04': 0,
                         'x_force_05': 0, 'x_force_06': 0,
                         'rise_xman_01': 0, 'rise_xman_02': 0, 'rise_xman_03': 0, 'rise_xman_04': 0,
                         'rise_xman_05': 0, 'rise_xman_06': 0}
                }

# print(game_log['max'], '\n', game_log[1])

'''
시작조건
 - 처음 실행할 때는 _do의 수가 모두 0으로 입력
 - 저장 파일이 어제 날짜라면, 시작조건에 해당
유지조건
 - 게임의 루프가 진행될 때마다 _do를 증분시키고 로그 파일을 저장하자
종료조건
 - 계정 번호의 최대값과 _do의 차가 0이라면 실행하지 않는다
'''

# print('first_family_01', game_log[1]['first_family_01'])


# def write_file(data, file_path):
#     with open(file_path, 'w', encoding='utf-8') as write_json:
#         try:
#             # write_json.write('\n'.join([json.dumps(d) for d in data]))
#             pickle.dump(data, write_json)
#         except:
#             print('Err occured')
#         finally:
#             pass
#
#
# write_file(game_log, 'game_log.txt')

# def save_log():
#     # log_dict = json.dumps(game_log)
#     with open('game_log.pickle', 'wb') as f:
#         pickle.dump(game_log, f)


# save_log()

pickle.dump(game_log, open('game_log.pickle', 'wb'))


to utils

# def go_home():
#     # go to home if not home
#     time.sleep(random.uniform(0.2, 0.5))
#     check_click_v2('go_home.jpg')
#     time.sleep(random.uniform(0.5, 1.5))

# def check_click_v2(filename):
#     button = pag.locateOnScreen(os.path.join('buttons/', filename), grayscale=True, confidence=.9)
#     print(filename, button)
#     # Box(left=1416, top=562, width=50, height=41)
#     if button is not None:
#         try:
#             mouse_click(button[0] + button[2] / 2 + random.uniform(0, button[2] * 0.3),
#                         button[1] + button[3] / 2 + random.uniform(0, button[3] * 0.3))
#         finally:
#             pass

def wait_click(filename):
    while True:
        if pag.locateOnScreen(os.path.join('buttons/', filename), grayscale=True, confidence=.9):
            time.sleep(random.uniform(1.1, 1.5))
            check_click(filename)
            time.sleep(random.uniform(0.1, 0.5))
            if pag.locateOnScreen(os.path.join('buttons/', filename), grayscale=True, confidence=.9) is None:
                break
        else:
            time.sleep(random.uniform(0.5, 1))


def check_click(filename):
    # 버튼의 이미지가 있다면, 화면에서 해당 버튼의 좌표를 산출할 수 있다.
    # https://pyautogui.readthedocs.io/en/latest/screenshot.html
    # pass_over_button = pag.locateOnScreen('button_pass_over.jpg')
    button = pag.locateOnScreen(os.path.join('buttons/', filename), grayscale=True, confidence=.9)
    print(os.path.join('buttons/', filename), button)
    # https://automatetheboringstuff.com/chapter18/
    # locateOnScreen은 이미지가 완벽하게 매칭되어야 함 ㅠㅠ
    # Note that the image on the screen must match the provided image perfectly in order to be recognized.

    # Box(left=1416, top=562, width=50, height=41)
    if button is not None:
        try:
            print(button[0])
            mouse_click(button[0] + button[2]/2 + random.uniform(0, button[2]*0.3),
                        button[1] + button[3]/2 + random.uniform(0, button[3]*0.3))
            # pag.moveTo(x=pass_over_button[0], y=pass_over_button[1])
        finally:
            pass

def mouse_click(pos_x, pos_y):
    x, y = pag.position()
    pag.moveTo(pos_x, pos_y)
    pag.mouseDown()
    # time.sleep(random.uniform(1.01, 2.23))
    time.sleep(random.uniform(0.21, 0.43))
    pag.mouseUp()
    pag.moveTo(x, y)

"""
