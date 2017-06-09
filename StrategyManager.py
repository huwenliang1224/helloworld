#!/usr/bin/python
# coding=utf-8

import time
import xml.dom.minidom
from xml.dom.minidom import parse
import CommonUtil
import RedisUtil


def generateStrategy(isCluster, update, sname):
    DOMTree = xml.dom.minidom.parse(sname + "/strategy.xml")
    strategy = DOMTree.documentElement

    # strategy_type
    strategy_type = ''
    try:
        strategy_type = strategy.getElementsByTagName('strategy_type')[0].childNodes[0].data
    except Exception as e:
        print(e)

    print("strategy_type:" + strategy_type)

    # dsp_name
    dsp_name = ''
    try:
        dsp_name = strategy.getElementsByTagName('dsp_name')[0].childNodes[0].data
    except Exception as e:
        print(e)

    print("dsp_name:" + dsp_name)

    # dsp_id
    dsp_id = ''
    try:
        dsp_id = strategy.getElementsByTagName('dsp_id')[0].childNodes[0].data
    except Exception as e:
        print(e)

    print("dsp_id:" + dsp_id)

    # token
    token = ''
    try:
        token = strategy.getElementsByTagName('token')[0].childNodes[0].data
    except Exception as e:
        print(e)

    print("token:" + token)

    # pkg_name
    pkg_name = ''
    try:
        pkg_name = strategy.getElementsByTagName('pkg_name')[0].childNodes[0].data
    except Exception as e:
        print(e)

    print("pkg_name:" + pkg_name)

    # concurrency
    concurrency = '-1'
    try:
        concurrency = strategy.getElementsByTagName('concurrency')[0].childNodes[0].data
    except Exception as e:
        print(e)

    print("concurrency:" + concurrency)

    # req_url
    req_url = ''
    try:
        req_url = strategy.getElementsByTagName('req_url')[0].childNodes[0].data
    except Exception as e:
        print(e)

    print("req_url:" + req_url)

    # top
    top = '-1'
    try:
        top = strategy.getElementsByTagName('top')[0].childNodes[0].data
    except Exception as e:
        print(e)

    print("top:" + top)

    # ids
    ids = []
    try:
        ids_e = strategy.getElementsByTagName('ids')[0].getElementsByTagName('id')
        for id_e in ids_e:
            id = id_e.childNodes[0].data
            ids.append(id)
    except Exception as e:
        print(e)

    print("ids:" + ','.join(ids))

    # base
    base = '0'
    try:
        base = strategy.getElementsByTagName('base')[0].childNodes[0].data
    except Exception as e:
        print(e)

    print("base:" + base)

    # mac
    macfiles = []
    has_mac = '-1'
    try:
        files_e = strategy.getElementsByTagName('mac')[0].getElementsByTagName('files')[0].getElementsByTagName(
            'file')
        for file_e in files_e:
            filename = file_e.childNodes[0].data
            with open(sname + '/mac.txt') as file:
                for line in file:
                    macfiles.append(line.rstrip('\n'))
        if (len(macfiles) > 0):
            has_mac = '1'
    except Exception as e:
        print(e)

    print("macfiles:" + ','.join(macfiles))

    # exclude_mac
    exclude_mac_files = []
    has_exclude_mac = '-1'
    try:
        files_e = strategy.getElementsByTagName('exclude_mac')[0].getElementsByTagName('files')[
            0].getElementsByTagName(
            'file')
        for file_e in files_e:
            filename = file_e.childNodes[0].data
            with open(sname + '/exclude_mac.txt') as file:
                for line in file:
                    exclude_mac_files.append(line.rstrip('\n'))
        if (len(exclude_mac_files) > 0):
            has_exclude_mac = '1'
    except Exception as e:
        print(e)

    print("exclude_mac_files:" + ','.join(exclude_mac_files))

    # area
    areas = []
    has_area = '-1'

    try:
        areas_e = strategy.getElementsByTagName('area')[0].getElementsByTagName('areas')[0].getElementsByTagName(
            'area')
        for area_e in areas_e:
            area = area_e.childNodes[0].data
            areas.append(area)
        if (len(areas) > 0):
            has_area = '1'
    except Exception as e:
        print(e)

    print("areas:" + ','.join(areas))

    # exclude_area
    exclude_areas = []
    has_exclude_area = '-1'

    try:
        exclude_area_e = strategy.getElementsByTagName('exclude_area')[0].getElementsByTagName('areas')[
            0].getElementsByTagName(
            'area')
        for area_e in exclude_area_e:
            area = area_e.childNodes[0].data
            exclude_areas.append(area)
        if (len(exclude_areas) > 0):
            has_exclude_area = '1'
    except Exception as e:
        print(e)

    print("exclude_areas:" + ','.join(exclude_areas))

    # daily
    daily_start = '-1'
    daily_end = '-1'

    try:
        daily_e = strategy.getElementsByTagName('daily')[0]
        start_e = daily_e.getElementsByTagName('start')[0]
        daily_start = start_e.childNodes[0].data
        end_e = daily_e.getElementsByTagName('end')[0]
        daily_end = end_e.childNodes[0].data
    except Exception as e:
        print(e)

    print("daily_start:" + daily_start)
    print("daily_end:" + daily_end)

    # time
    tstart = '-1'
    tend = '-1'

    try:
        time_e = strategy.getElementsByTagName('time')[0]
        start_e = time_e.getElementsByTagName('start')[0]
        end_e = time_e.getElementsByTagName('end')[0]

        tstart = start_e.childNodes[0].data
        tend = end_e.childNodes[0].data

        startTimeArray = time.strptime(tstart, "%Y/%m/%d %H:%M:%S")
        endTimeArray = time.strptime(tend, "%Y/%m/%d %H:%M:%S")

        tstart = str(int(round(time.mktime(startTimeArray) * 1000)))
        tend = str(int(round(time.mktime(endTimeArray) * 1000)))
    except Exception as e:
        print(e)

    print("time_start:" + tstart)
    print("time_end:" + tend)

    # img
    imgs = []

    try:
        imgs_e = strategy.getElementsByTagName('img')[0].getElementsByTagName('imgs')[0].getElementsByTagName(
            'img')
        for img_e in imgs_e:
            img = img_e.childNodes[0].data
            imgs.append(img)
    except Exception as e:
        print(e)

    print("imgs:" + ','.join(imgs))

    # material_type
    material_type = ''
    try:
        material_type = strategy.getElementsByTagName('material_type')[0].childNodes[0].data
    except Exception as e:
        print(e)

    print("material_type:" + material_type)

    # material_title
    material_title = ''
    try:
        material_title = strategy.getElementsByTagName('material_title')[0].childNodes[0].data
    except Exception as e:
        print(e)

    print("material_title:" + material_title)

    # material_desc
    material_desc = ''
    try:
        material_desc = strategy.getElementsByTagName('material_desc')[0].childNodes[0].data
    except Exception as e:
        print(e)

    print("material_desc:" + material_desc)

    # material_icon
    material_icon = ''
    try:
        material_icon = strategy.getElementsByTagName('material_icon')[0].childNodes[0].data
    except Exception as e:
        print(e)

    print("material_icon:" + material_icon)

    # win_notice_url
    winNoticeUrls = []

    try:
        win_notice_urls_e = strategy.getElementsByTagName('win_notice_url')[0].getElementsByTagName('urls')[
            0].getElementsByTagName(
            'url')
        for url_e in win_notice_urls_e:
            url = url_e.childNodes[0].data
            winNoticeUrls.append(url)
    except Exception as e:
        print(e)

    print("win_notice_url:" + ','.join(winNoticeUrls))

    # click_notice_url
    click_notice_url = []

    try:
        click_notice_urls_e = strategy.getElementsByTagName('click_notice_url')[0].getElementsByTagName('urls')[
            0].getElementsByTagName(
            'url')
        for url_e in click_notice_urls_e:
            url = url_e.childNodes[0].data
            click_notice_url.append(url)
    except Exception as e:
        print(e)

    print("click_notice_url:" + ','.join(click_notice_url))

    # click_url
    click_url = ''
    try:
        click_url = strategy.getElementsByTagName('click_url')[0].childNodes[0].data
    except Exception as e:
        print(e)

    print("click_url:" + click_url)

    # weight
    weight = '0'
    try:
        weight = strategy.getElementsByTagName('weight')[0].childNodes[0].data
    except Exception as e:
        print(e)

    print("weight:" + weight)

    strategy_id = "strategy." + sname
    print("strategy_id:" + strategy_id)

    # =====start insert to redis======
    print("=====start insert to redis======")

    redis = RedisUtil.newInstance(isCluster)

    current = redis.get(strategy_id + ".current")

    if (CommonUtil.isNotBlank(current)):
        try:
            int(current)
        except:
            current = "0"

    delete(isCluster, sname)

    redis.set(strategy_id + ".strategy_type", strategy_type)
    redis.set(strategy_id + ".weight", weight)
    redis.set(strategy_id + ".dsp_name", dsp_name)
    redis.set(strategy_id + ".dsp_id", dsp_id)
    redis.set(strategy_id + ".token", token)
    redis.set(strategy_id + ".pkg_name", pkg_name)
    redis.set(strategy_id + ".concurrency", concurrency)
    redis.set(strategy_id + ".req_url", req_url)

    redis.set(strategy_id + ".top", top)

    redis.set(strategy_id + ".current", current if update else '0')

    for id in ids:
        redis.hset(strategy_id + ".ids", id, "")

    redis.set(strategy_id + ".base", base)

    for mac in macfiles:
        redis.hset(strategy_id + ".mac.macs", mac, "")

    for exclude_mac in exclude_mac_files:
        redis.hset(strategy_id + ".exclude_mac.macs", exclude_mac, "")

    for area in areas:
        redis.hset(strategy_id + ".area.areas", area, "")

    for exclude_area in exclude_areas:
        redis.hset(strategy_id + ".exclude_area.areas", exclude_area, "")

    redis.set(strategy_id + ".has_exclude_mac", has_exclude_mac)
    redis.set(strategy_id + ".has_mac", has_mac)
    redis.set(strategy_id + ".has_area", has_area)
    redis.set(strategy_id + ".has_exclude_area", has_exclude_area)

    redis.set(strategy_id + ".daily.start", daily_start)
    redis.set(strategy_id + ".daily.end", daily_end)

    redis.set(strategy_id + ".time.start", tstart)
    redis.set(strategy_id + ".time.end", tend)

    for im in imgs:
        redis.hset(strategy_id + ".img.imgs", im, "")

    for nu in winNoticeUrls:
        redis.hset(strategy_id + ".win_notice_url.urls", nu, "")

    for nu in click_notice_url:
        redis.hset(strategy_id + ".click_notice_url.urls", nu, "")

    redis.set(strategy_id + ".click_url", click_url)
    redis.set(strategy_id + ".material_icon", material_icon)
    redis.set(strategy_id + ".material_title", material_title)
    redis.set(strategy_id + ".material_desc", material_desc)
    redis.set(strategy_id + ".material_type", material_type)

    redis.hset("strategies", strategy_id, "1")  # global set

    look(isCluster, sname)


def delete(isCluster, sname):
    try:
        redis = RedisUtil.newInstance(isCluster)
        strategy_id = "strategy." + sname
        redis.hdel("strategies", strategy_id)  # global hset

        redis.delete(strategy_id + ".strategy_type")
        redis.delete(strategy_id + ".weight")
        redis.delete(strategy_id + ".dsp_name")
        redis.delete(strategy_id + ".dsp_id")
        redis.delete(strategy_id + ".token")
        redis.delete(strategy_id + ".pkg_name")
        redis.delete(strategy_id + ".concurrency")
        redis.delete(strategy_id + ".req_url")
        redis.delete(strategy_id + ".top")
        redis.delete(strategy_id + ".current")
        redis.delete(strategy_id + ".ids")  # hset
        redis.delete(strategy_id + ".base")
        redis.delete(strategy_id + ".mac.macs")  # hset
        redis.delete(strategy_id + ".exclude_mac.macs")  # hset
        redis.delete(strategy_id + ".area.areas")  # hset
        redis.delete(strategy_id + ".exclude_area.areas")  # hset

        redis.delete(strategy_id + ".has_exclude_mac")
        redis.delete(strategy_id + ".has_mac")
        redis.delete(strategy_id + ".has_area")
        redis.delete(strategy_id + ".has_exclude_area")

        redis.delete(strategy_id + ".daily.start")
        redis.delete(strategy_id + ".daily.end")
        redis.delete(strategy_id + ".time.start")
        redis.delete(strategy_id + ".time.end")
        redis.delete(strategy_id + ".img.imgs")  # hset
        redis.delete(strategy_id + ".notice_url.urls")  # hset
        redis.delete(strategy_id + ".win_notice_url.urls")  # hset
        redis.delete(strategy_id + ".click_notice_url.urls")  # hset
        redis.delete(strategy_id + ".click_url")

        redis.delete(strategy_id + ".material_icon")
        redis.delete(strategy_id + ".material_title")
        redis.delete(strategy_id + ".material_desc")
        redis.delete(strategy_id + ".material_type")
    except:
        raise Exception('delete error')


def look(isCluster, sname):
    try:
        redis = RedisUtil.newInstance(isCluster)
        strategy_id = "strategy." + sname
        print("strategy_id:" + strategy_id)

        print("strategies." + strategy_id + ":" + redis.hget("strategies", strategy_id))

        print(strategy_id + ".strategy_type:" + redis.get(strategy_id + ".strategy_type"))
        print(strategy_id + ".weight:" + redis.get(strategy_id + ".weight"))
        print(strategy_id + ".dsp_name:" + redis.get(strategy_id + ".dsp_name"))
        print(strategy_id + ".dsp_id:" + redis.get(strategy_id + ".dsp_id"))
        print(strategy_id + ".token:" + redis.get(strategy_id + ".token"))
        print(strategy_id + ".pkg_name:" + redis.get(strategy_id + ".pkg_name"))
        print(strategy_id + ".concurrency:" + redis.get(strategy_id + ".concurrency"))
        print(strategy_id + ".req_url:" + redis.get(strategy_id + ".req_url"))
        print(strategy_id + ".top:" + redis.get(strategy_id + ".top"))
        print(strategy_id + ".current:" + redis.get(strategy_id + ".current"))

        ids_map = redis.hgetAll(strategy_id + ".ids")
        if (ids_map is not None and len(ids_map) > 0):
            for id in ids_map:
                print('code_id:' + id)
        else:
            print("no code_id")

        print(strategy_id + ".base:" + redis.get(strategy_id + ".base"))

        print(strategy_id + ".has_area:" + redis.get(strategy_id + ".has_area"))
        print(strategy_id + ".has_exclude_area:" + redis.get(strategy_id + ".has_exclude_area"))
        print(strategy_id + ".has_mac:" + redis.get(strategy_id + ".has_mac"))
        print(strategy_id + ".has_exclude_mac:" + redis.get(strategy_id + ".has_exclude_mac"))

        print(strategy_id + ".daily.start:" + redis.get(strategy_id + ".daily.start"))
        print(strategy_id + ".daily.end:" + redis.get(strategy_id + ".daily.end"))

        system_time = time.time()

        print("daily.now:" + str(int(round(system_time * 1000))))

        print(strategy_id + ".time.start:" + redis.get(strategy_id + ".time.start"))
        print(strategy_id + ".time.end:" + redis.get(strategy_id + ".time.end"))

        print("time.now:" + time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(system_time)))

        img_imgs_map = redis.hgetAll(strategy_id + ".img.imgs")
        if (len(img_imgs_map) > 0):
            for img in img_imgs_map:
                print('img:' + img)
        else:
            print("no img")

        win_notice_url_urls_map = redis.hgetAll(strategy_id + ".win_notice_url.urls")
        if (len(win_notice_url_urls_map) > 0):
            for url in win_notice_url_urls_map:
                print('win_notice_url:' + url)
        else:
            print("no win_notice_url")

        click_notice_url_urls_map = redis.hgetAll(strategy_id + ".click_notice_url.urls")
        if (len(click_notice_url_urls_map) > 0):
            for url in click_notice_url_urls_map:
                print('click_notice_url:' + url)
        else:
            print("no click_notice_url")

        print(strategy_id + ".click_url:" + redis.get(strategy_id + ".click_url"))
        print(strategy_id + ".material_icon:" + redis.get(strategy_id + ".material_icon"))
        print(strategy_id + ".material_title:" + redis.get(strategy_id + ".material_title"))
        print(strategy_id + ".material_desc:" + redis.get(strategy_id + ".material_desc"))
        print(strategy_id + ".material_type:" + redis.get(strategy_id + ".material_type"))
    except Exception as e:
        print(e)
        raise Exception('look error')


def drop(isCluster, sname):
    try:
        print("=====start delete from redis======")
        delete(isCluster, sname)
    except:
        raise Exception('drop error')


if __name__ == '__main__':
    generateStrategy(False, False, 'toutiao')
