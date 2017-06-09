#!/usr/bin/python
# coding=utf-8

from xml.dom.minidom import parse
import xml.dom.minidom


def generateStrategy(update, sname):
    DOMTree = xml.dom.minidom.parse("strategy.xml")
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
        files_e = strategy.getElementsByTagName('mac')[0].getElementsByTagName('files')[0].getElementsByTagName('file')
        for file_e in files_e:
            filename = file_e.childNodes[0].data
            with open('mac.txt') as file:
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
        files_e = strategy.getElementsByTagName('exclude_mac')[0].getElementsByTagName('files')[0].getElementsByTagName(
            'file')
        for file_e in files_e:
            filename = file_e.childNodes[0].data
            with open('exclude_mac.txt') as file:
                for line in file:
                    exclude_mac_files.append(line.rstrip('\n'))
        if (len(exclude_mac_files) > 0):
            has_exclude_mac = '1'
    except Exception as e:
        print(e)

    print("exclude_mac_files:" + ','.join(exclude_mac_files))

    # area
    areas = []
    has_area = '-1';

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
    has_exclude_area = '-1';

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
        import time

        time_e = strategy.getElementsByTagName('time')[0]
        start_e = time_e.getElementsByTagName('start')[0]
        end_e = time_e.getElementsByTagName('end')[0]

        tstart = start_e.childNodes[0].data
        tend = end_e.childNodes[0].data

        startTimeArray = time.strptime(tstart, "%Y/%m/%d %H:%M:%S")
        endTimeArray = time.strptime(tend, "%Y/%m/%d %H:%M:%S")

        tstart = str(int(time.mktime(startTimeArray)) * 1000)
        tend = str(int(time.mktime(endTimeArray)) * 1000)
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
