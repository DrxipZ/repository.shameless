# -*- coding: utf-8 -*-
import xbmcaddon,os,xbmc,xbmcgui,urllib,re,xbmcplugin,sys,logging,json
__USERAGENT__ = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11'
__addon__ = xbmcaddon.Addon()
__cwd__ = xbmc.translatePath(__addon__.getAddonInfo('path'))
Addon = xbmcaddon.Addon()
user_dataDir = xbmc.translatePath(Addon.getAddonInfo("profile"))
if not os.path.exists(user_dataDir):
     os.makedirs(user_dataDir)
import requests
KODI_VERSION = int(xbmc.getInfoLabel("System.BuildVersion").split('.', 1)[0])
base_image='https://ws0.cocoscope.com/covers/63934.jpg'
base_icon='http://dabutcher.org/coco/fanart.png'
base_image_kodiapps='https://kodiapps.com/images/logo.png'
base_icon_kodiapps='https://kodiapps.com/images/logo.png'

dab_cat=['19 Help','Must-have','Build','Streaming Matters','Tips And Tricks','Everyting else']
dab_cat_names=['Matrix Kodi 19 Stuff','Must Have','Builds','Streaming Matters','Tips And Tricks','Everything Else']
kodiapps_cat=['Build','Skin','Wizard','Everyting else']
kodiapps_cat_names=['Build','Skin','Wizard','Everyting else']

if KODI_VERSION<=18:
    
    que=urllib.quote_plus
    que_n=urllib.quote
    url_encode=urllib.urlencode
    unque=urllib.unquote_plus
else:
    
    que_n=urllib.parse.quote
    que=urllib.parse.quote_plus
    url_encode=urllib.parse.urlencode
    unque=urllib.parse.unquote_plus
def get_params():
        param=[]
        if len(sys.argv)>=2:
          paramstring=sys.argv[2]
          if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param     
def utf8_urlencode(params):
    try:
        import urllib as u
        enc=u.urlencode
    except:
        from urllib.parse import urlencode
        enc=urlencode
    # problem: u.urlencode(params.items()) is not unicode-safe. Must encode all params strings as utf8 first.
    # UTF-8 encodes all the keys and values in params dictionary
    for k,v in list(params.items()):
        # TRY urllib.unquote_plus(artist.encode('utf-8')).decode('utf-8')
        if type(v) in (int, float):
            params[k] = v
        else:
            try:
                params[k.encode('utf-8')] = v.encode('utf-8')
            except Exception as e:
                pass
                #logging.warning( '**ERROR utf8_urlencode ERROR** %s' % e )
    
    return enc(params).encode().decode('utf-8')
def addNolink( name, url,mode,isFolder, iconimage="DefaultFolder.png",fanart="DefaultFolder.png"):
 

          
         
          u=sys.argv[0]+"?url="+que(url)+"&mode="+str(mode)+"&name="+que(name)
          if KODI_VERSION<=18:
            liz = xbmcgui.ListItem( name, iconImage=iconimage, thumbnailImage=iconimage)
          else:
            liz = xbmcgui.ListItem( name)
          liz.setInfo(type="Video", infoLabels={ "Title": unque( name)   })
          liz.setProperty( "Fanart_Image", fanart )
          art = {}
          art.update({'poster': iconimage,'icon': iconimage,'thumb': iconimage})
          liz.setArt(art)
          liz.setProperty("IsPlayable","false")
          liz.setProperty( "Fanart_Image", iconimage )
          xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz,isFolder=isFolder)
###############################################################################################################        

def addDir3(name,url,mode,iconimage,fanart,description,page='0'):
        params={}
        params['url']=url
        params['mode']=mode
        params['name']=name
        params['data']=data
        params['iconimage']=iconimage
        params['fanart']=fanart
        params['description']=description
        params['page']=page
        all_ur=utf8_urlencode(params)
        u=sys.argv[0]+"?mode="+str(mode)+'&'+all_ur
          
        
        ok=True
        if KODI_VERSION<=18:
            liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        else:
            liz=xbmcgui.ListItem(name)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        art = {}
        art.update({'poster': iconimage,'icon': iconimage,'thumb': iconimage})
        liz.setArt(art)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        
        return ok



def addLink( name, url,mode,isFolder, iconimage,fanart,description,data=''):
          params={}
          params['url']=url

          params['name']=name
          params['data']=data
          params['iconimage']=iconimage
          params['fanart']=fanart
          params['description']=description
          
          all_ur=utf8_urlencode(params)
          u=sys.argv[0]+"?mode="+str(mode)+'&'+all_ur
          
          menu_items=[]
          menu_items.append(('Video Info', 'RunPlugin(%s)' % (sys.argv[0]+"?mode="+str(4)+'&'+all_ur)))
          menu_items.append(('Install repo', 'RunPlugin(%s)' % (sys.argv[0]+"?mode="+str(11)+'&'+all_ur)))
          menu_items.append(('Add to kodi source', 'RunPlugin(%s)' % (sys.argv[0]+"?mode="+str(3)+'&'+all_ur)))
          video_info={}
         
          video_info['title']=name
          video_info['plot']=description
       
          
          #u=sys.argv[0]+"?url="+que(url)+"&mode="+str(mode)+"&name="+que(name)
          if KODI_VERSION<=18:
            liz = xbmcgui.ListItem( name, iconImage=iconimage, thumbnailImage=iconimage)
          else:
            liz = xbmcgui.ListItem( name)
          liz.addContextMenuItems(menu_items, replaceItems=False)
          liz.setInfo(type="Video", infoLabels=video_info)
          art = {}
          art.update({'poster': iconimage,'icon': iconimage,'thumb': iconimage})
          liz.setArt(art)
          liz.setProperty("IsPlayable","true")
          liz.setProperty( "Fanart_Image", fanart )
          xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz,isFolder=isFolder)


def read_site_html(url_link):
    '''
    req = urllib2.Request(url_link)
    req.add_header('User-agent',__USERAGENT__)# 'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30')
    html = urllib2.urlopen(req).read()
    '''
    import requests
    html=requests.get(url_link).content
    return html

def main_menu():
    addDir3( "[COLOR lightblue]DaB's Videos[/COLOR]", 'Dabs',5, base_icon,base_image,"Dab's videos")
    addDir3( "[COLOR lightblue]Kodiapps Videos[/COLOR]", 'Kodiapps',5, base_icon_kodiapps,base_image_kodiapps,"Dab's videos")
def next_level(url,icon,fan):
    addDir3( "[COLOR lightblue]All[/COLOR]", url+'$$$0',7, icon,fan,'All videos')
    if url=='Dabs':
      count=0
      for items in dab_cat:
        addDir3( "[COLOR lightblue]%s[/COLOR]"%dab_cat_names[count], 'Dabs$$$'+items,6, base_icon,base_image,items)
        count+=1
      addDir3( "[COLOR lightblue]Youtube Channel[/COLOR]", 'https://www.youtube.com/channel/UC-jBkGiRokRd-B2ylx1VqJQ',8, base_icon,base_image,items)
    else:
        count=0
        for items in kodiapps_cat:
            addDir3( "[COLOR lightblue]%s[/COLOR]"%kodiapps_cat_names[count], 'kodiapps$$$'+items,6, base_icon_kodiapps,base_image_kodiapps,items)
            count+=1
def populate(url): 
    chan=url.split('$$$')[0]
    tested_array=[]
    if chan=='Dabs':
        chan_id='63934'
        for items in dab_cat:
            tested_array.append(items.lower())
            
    else:
        chan_id='295353'
        for items in kodiapps_cat:
            tested_array.append(items.lower())
    
    cat=url.split('$$$')[1]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers',
    }
    
        
    for page in range(0,50):
        found=False
        
        params = (
            ('layout', 'blank'),
            ('controller', 'ajax'),
            ('action', 'get_videos'),
            ('offset', str(page*24)),
            ('category_id', '0'),
            ('channel_id', chan_id),
            ('sort_id', 'date'),
            ('status', '0'),
            ('videos_per_load', '24'),
        )

        response = requests.get('https://www.cocoscope.com/', headers=headers, params=params,verify=False).json()
        for items in response:
            found=True
            lk=items['id']
            
            nm=items['name']
            if cat=='Everyting else':
                cont=False
                for it in tested_array:
                    logging.warning('it:'+it)
                    if  it.replace('-',' ') in nm.lower() :
                        cont=True
                        break
                    if cont:
                        break
                if cont:
                    continue
            else:
                if cat.lower().replace('-',' ') not in nm.lower():
                    continue
            ic=items['thumbnail_url']
            plot=items['fancy_date_2']+'\n'+items['view_string']+'\n'+items['time_elapsed']
            addLink( nm, lk,2,False, ic,ic,plot)
        if not found:
            break
        #addDir3( '[COLOR lightblue]Next Page[/COLOR]', str(int(page+1)),'0', base_icon,base_image,'Next Page')
def download_zip(url):
    import requests
    logging.warning('url::'+url)
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }
    path=os.path.join(user_dataDir,'install_file.zip')
    r = requests.get(url, headers=headers,allow_redirects=True)
    open(path, 'wb').write(r.content)
    return path
def copyDirTree(root_src_dir,root_dst_dir):
    import shutil
    """
    Copy directory tree. Overwrites also read only files.
    :param root_src_dir: source directory
    :param root_dst_dir:  destination directory
    """
    not_copied=[]
    for src_dir, dirs, files in os.walk(root_src_dir):
        dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file_ in files:
            
        
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                try:
                    os.remove(dst_file)
                except Exception as exc:
                    #os.chmod(dst_file, stat.S_IWUSR)
                    #os.remove(dst_file)
                    logging.warning('Error del:'+dst_file)
                    logging.warning(exc)
            try:
                shutil.copy(src_file, dst_dir)
            except:
              if '.dll' not in file_ and '.so' not in file_:
                not_copied.append(file_)
    return not_copied
def dis_or_enable_addon(addon_id, enable="true"):
    import json
    logging.warning('ADDON ID:'+addon_id)
    addon = '"%s"' % addon_id
    if xbmc.getCondVisibility("System.HasAddon(%s)" % addon_id) and enable == "true":
        logging.warning('already Enabled')
        return xbmc.log("### Skipped %s, reason = allready enabled" % addon_id)
    elif not xbmc.getCondVisibility("System.HasAddon(%s)" % addon_id) and enable == "false":
        return xbmc.log("### Skipped %s, reason = not installed" % addon_id)
    else:
        do_json = '{"jsonrpc":"2.0","id":1,"method":"Addons.SetAddonEnabled","params":{"addonid":%s,"enabled":%s}}' % (addon, enable)
        logging.warning(do_json)
        query = xbmc.executeJSONRPC(do_json)
        response = json.loads(query)
        if enable == "true":
            logging.warning("### Enabled %s, response = %s" % (addon_id, response))
        else:
            logging.warning("### Disabled %s, response = %s" % (addon_id, response))
    return xbmc.executebuiltin('Container.Update(%s)' % xbmc.getInfoLabel('Container.FolderPath'))
def install_addon(name,url,silent=False,Delete=True):
  import xbmcvfs,time,shutil
  try:
    try:
        from zfile_18 import ZipFile
    except:
        import zipfile
        from zipfile import ZipFile
    addon_extract_path=os.path.join(user_dataDir, 'addons','temp')
    if not xbmcvfs.exists(addon_extract_path+'/'):
         os.makedirs(addon_extract_path)
    addon_path=os.path.join(user_dataDir, 'addons')
    if not xbmcvfs.exists(addon_path+'/'):
         os.makedirs(addon_path)
       
    #Install
   
    
    
    if 1:
        if silent==False:
            dp = xbmcgui.DialogProgress()
            dp.create('Dabscope', '[B][COLOR=yellow]Installing[/COLOR][/B]')
        if Delete:
            try:
                if os.path.exists(addon_path):
                    shutil.rmtree(addon_path)
            except Exception as e:
                logging.warning('error removing folder:'+str(addon_path)+','+str(e))
            if not xbmcvfs.exists(addon_path+'/'):
                os.makedirs(addon_path)
        mv_name=os.path.join(addon_path,name)
        
        addon=download_zip(url)
        
        if silent==False:
            dp.update(0,'[B][COLOR=green]Dabscope[/COLOR][/B]'+'\n'+ '[B][COLOR=yellow]Extracting[/COLOR][/B]')
        zf = ZipFile(addon)

        uncompress_size = sum((file.file_size for file in zf.infolist()))

        extracted_size = 0

        for file in zf.infolist():
            extracted_size += file.file_size
            if silent==False:
                dp.update(int((extracted_size*100.0)/uncompress_size),'[B][COLOR=green]Dabscope[/COLOR][/B]'+'\n'+ '[B][COLOR=yellow]Extracting[/COLOR][/B]'+'\n'+file.filename)
            
            zf.extract(member=file, path=addon_extract_path)
        zf.close()
        f_o = os.listdir(addon_extract_path)
        
            
        file = open(os.path.join(addon_extract_path,f_o[0], 'addon.xml'), 'r') 
        file_data= file.read()
        file.close()
        regex='id=(?:"|\')(.+?)(?:"|\')'
        nm=re.compile(regex).findall(file_data)[0]
        if not xbmc.getCondVisibility("System.HasAddon(%s)" % name.split('-')[0]):
            regex='import addon=(?:"|\')(.+?)(?:"|\')'
            dep=re.compile(regex).findall(file_data)
            missing=[]
            if silent==False:
                dp.update(90,'[B][COLOR=green]Dabscope[/COLOR][/B]'+'\n'+ '[B][COLOR=yellow]Dependencies[/COLOR][/B]')
            zzz=0
            for items in dep:
                if silent==False:
                    dp.update(int((extracted_size*100.0)/len(items)),'[B][COLOR=green]Dabscope[/COLOR][/B]'+'\n'+ '[B][COLOR=yellow]Dependencies[/COLOR][/B]'+'\n'+items)
                zzz+=1
                if not xbmc.getCondVisibility("System.HasAddon(%s)" % items):
                    missing.append(items)
            if len(missing)>0:
                showText('Missing Dependencies','\n'.join(missing))
                return 0
        addon_p=xbmc.translatePath("special://home/addons/")
        
        
        files = os.listdir(addon_extract_path)
        logging.warning(os.path.join(addon_p,f_o[0]))
        
        logging.warning('Copy')
        not_copied=copyDirTree(os.path.join(addon_extract_path,f_o[0]),os.path.join( addon_p,f_o[0]))
        if len(not_copied)>0:
            showText('File That was not copied', '\n'.join(not_copied))
        
        xbmc.executebuiltin("UpdateLocalAddons()")
        if silent==False:
            dp.update(100,'[B][COLOR=green]Dabscope[/COLOR][/B]'+'\n'+ '[B][COLOR=yellow]Cleaning[/COLOR][/B]')
        time.sleep(1)
        dis_or_enable_addon(nm)
        shutil.rmtree(addon_path)
        if silent==False:
            dp.close()
        #'Installed'
        #'Installation complete'
        if silent==False:
            xbmcgui.Dialog().ok('Dabscope','Done')
  except Exception as e:
            import linecache,sys
            exc_type, exc_obj, tb = sys.exc_info()
            f = tb.tb_frame
            lineno = tb.tb_lineno
            filename = f.f_code.co_filename
            linecache.checkcache(filename)
            line = linecache.getline(filename, lineno, f.f_globals)
            logging.warning('ERROR IN Auto Install defualt:'+str(lineno))
            logging.warning('inline:'+str(line))
            logging.warning(str(e))
            in_install=0
def files_from(name,url,source=False):
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers',
    }

    params = (
        ('v', url),
    )
    if 'youtube' in url:
        all_l=[]
        response = requests.get(url, headers=headers).content.decode('utf-8')
        regex='"description":{"simpleText":(.+?)"'
        m=re.compile(regex,re.DOTALL).findall(response)[0]
    else:
        response = requests.get('https://www.cocoscope.com/watch', headers=headers, params=params,verify=False).content.decode('utf-8')
        regex='meta property="og:description" content="(.+?)"'
        m=re.compile(regex,re.DOTALL).findall(response)[0]
    
    m=m.split('\n')
    all_l=[]
    for itt in m:
        logging.warning(itt)
        regex='http(.+?)(?: |$)'
        all_links=re.compile(regex).findall(itt)
        if len(all_links)>0:
            if 't.me' in all_links[0] or 'twitter' in all_links[0]:
                continue
       
            all_l.append('http'+all_links[0])
    ret = xbmcgui.Dialog().select('Choose', all_l)
    if source:
        if ret!=-1:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
            }
          
            y=requests.get(all_l[ret].strip(), headers=headers).content.decode('utf-8')
            logging.warning(y)
            regex='a href="(.+?)"'
            m2=re.compile(regex).findall(y)
            al_l=[]
            for items in m2:
                if '.zip' not in items:
                    continue
                al_l.append(items)
            ret2 = xbmcgui.Dialog().select('Choose', al_l)
            if ret2!=-1:
                if all_l[ret].strip().endswith('/'):
                    n_addr=all_l[ret].strip()+al_l[ret2]
                else:
                    n_addr=all_l[ret].strip()+'/'+al_l[ret2]
                install_addon(al_l[ret2],n_addr)
            else:
                sys.exit()
    else:
        if ret!=-1:
            ok=xbmcgui.Dialog().yesno("Add as kodi source?",all_l[ret])
            
            if ok:
                
                    setting_path=xbmc.translatePath("special://userdata")
                    s_file=os.path.join(setting_path,'sources.xml')
                    
                    
                    
                    search_entered='Repo'
                    keyboard = xbmc.Keyboard(search_entered, 'Enter Source name')
                    keyboard.doModal()
                    if keyboard.isConfirmed():
                        if os.path.exists(s_file):
                            file = open(s_file, 'r') 
                            file_r= file.read()
                            file.close()
                            if all_l[ret] in file_r:
                                xbmcgui.Dialog().ok('Error ','Source already exists')
                                return 0
                            regex='<files>(.+?)</files>'
                            o_data=re.compile(regex,re.DOTALL).findall(file_r)[0]
                            
                            o_data_full='<files>%s</files>'
                            added_txt='''\
                            <source>
                                <name>%s</name>
                                <path pathversion="1">%s</path>
                                <allowsharing>true</allowsharing>
                            </source>
                            '''
                            f_lk=all_l[ret].replace('\n','').replace('\r','').replace('\t','').strip()
                            new_o_data=file_r.replace(o_data_full%o_data,o_data_full%(o_data+added_txt%(keyboard.getText(),f_lk)))
                        else:
                            new_o_data='''\
    <sources>
        <programs>
            <default pathversion="1"></default>
        </programs>
        <video>
            <default pathversion="1"></default>
        </video>
        <music>
            <default pathversion="1"></default>
        </music>
        <pictures>
            <default pathversion="1"></default>
        </pictures>
        <files>
            <default pathversion="1"></default>
            <source>
                <name>%s</name>
                <path pathversion="1">%s</path>
                <allowsharing>true</allowsharing>
            </source>
        </files>
    </sources>


                            '''
                            f_lk=all_l[ret].replace('\n','').replace('\r','').replace('\t','').strip()
                            new_o_data=new_o_data%(keyboard.getText(),f_lk)
                        file = open(s_file, 'w') 
                        file.write(new_o_data)
                        file.close()
                        xbmcgui.Dialog().ok('Done','Need to restart kodi for changes')
                
        else:
          sys.exit()
def play_youtube (O000OO0O0000OO0OO,name ):#line:3025
    logging.warning(O000OO0O0000OO0OO)
    if O000OO0O0000OO0OO .endswith ('/'):#line:3026
        O000OO0O0000OO0OO =O000OO0O0000OO0OO [:-1 ]#line:3027
    O00OO0O000OO000OO =O000OO0O0000OO0OO .split ('v=')[1 ]#line:3028
    O00O00OO00OO0OOOO ='plugin://plugin.video.youtube/play/?video_id='+O00OO0O000OO000OO #line:3029
 
    logging.warning(O00O00OO00OO0OOOO)
    O000O0000000O0O00 =xbmcgui .ListItem (path =O00O00OO00OO0OOOO )#line:3054
    O000O0000000O0O00 .setInfo (type ="Video",infoLabels ={"Title":(name )})#line:3055
    
    xbmcplugin .setResolvedUrl (int (sys .argv [1 ]),True ,O000O0000000O0O00 )#line:3056
def play_link(name,url,plot):
    logging.warning(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers',
    }

    params = (
        ('v', url),
    )

    response = requests.get('https://www.cocoscope.com/watch', headers=headers, params=params,verify=False).content.decode('utf-8')
    regex='source src="(.+?)"'
    m=re.compile(regex).findall(response)
    
    regex='meta property="og:description" content="(.+?)"'
    p=re.compile(regex,re.DOTALL).findall(response)[0]
    listItem = xbmcgui.ListItem(name, path=m[0]) 
 
    listItem.setInfo(type='Video', infoLabels={'title':name,'plot':p})


    listItem.setProperty('IsPlayable', 'true')

    xbmcplugin.setResolvedUrl(handle=int(sys.argv[1]), succeeded=True, listitem=listItem)
def showText(heading, text):
    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(100)
    win = xbmcgui.Window(id)
    retry = 50
    while (retry > 0):
        try:
            xbmc.sleep(10)
            retry -= 1
            win.getControl(1).setLabel(heading)
            win.getControl(5).setText(text)
            return
        except:
            pass
def video_data(name,url):
    logging.warning('url::'+url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers',
    }
    if 'youtube' in url:
        all_l=[]
        response = requests.get(url, headers=headers).content.decode('utf-8')
        regex='"description":{"simpleText":(.+?)"'
        all_l=re.compile(regex,re.DOTALL).findall(response)[0]
        regex='http(.+?)(?: |$|\n)'
        all_links=re.compile(regex).findall(all_l)
       
        if len(all_links)>0:
     
            if 'http'+all_links[0] in all_l:
                logging.warning('found')
            all_l=all_l+'\n[COLOR khaki][B]'+'http'+all_links[0]+'[/B][/COLOR]'
            logging.warning(all_l)
                
        showText('Description', (all_l))
    else:
        params = (
            ('v', url),
        )

        response = requests.get('https://www.cocoscope.com/watch', headers=headers, params=params,verify=False).content.decode('utf-8')
        regex='meta property="og:description" content="(.+?)"'
        m=re.compile(regex,re.DOTALL).findall(response)[0]
        
        m=m.split('\n')
        all_l=[]
        for itt in m:
     
            regex='http(.+?)(?: |$)'
            all_links=re.compile(regex).findall(itt)
            if len(all_links)>0:
                #if 't.me' in all_links[0] or 'twitter' in all_links[0]:
                #    continue
           
                all_l.append('[COLOR khaki][B]'+'http'+all_links[0]+'[/B][/COLOR]')
            else:
                all_l.append(itt)
    
        showText('Description', '\n'.join(all_l))
def all_videos(url,icon,image):
    chan=url.split('$$$')[0]
    page=url.split('$$$')[1]
    if chan=='Dabs':
        chan_id='63934'
        
            
    else:
        chan_id='295353'
        
    if not page:
        page=0
    page=int(page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers',
    }

    params = (
        ('layout', 'blank'),
        ('controller', 'ajax'),
        ('action', 'get_videos'),
        ('offset', str(page*24)),
        ('category_id', '0'),
        ('channel_id', chan_id),
        ('sort_id', 'date'),
        ('status', '0'),
        ('videos_per_load', '24'),
    )

    response = requests.get('https://www.cocoscope.com/', headers=headers, params=params,verify=False).json()
    for items in response:
        lk=items['id']
        nm=items['name']
        ic=items['thumbnail_url']
        plot=items['fancy_date_2']+'\n'+items['view_string']+'\n'+items['time_elapsed']
        addLink( nm, lk,2,False, ic,ic,plot)
    addDir3( '[COLOR lightblue]Next Page[/COLOR]',chan+'$$$'+ str(int(page+1)),7, base_icon,base_image,'Next Page')
def html_decode(s):
   
    """
    Returns the ASCII decoded version of the given HTML string. This does
    NOT remove normal HTML tags like <p>.
    """
    htmlCodes = (
            ("'", '&#39;'),
            ('"', '&quot;'),
            ('>', '&gt;'),
            ('<', '&lt;'),
            ('-','&#8211;'),
            ('&', '&amp;')
        )
    for code in htmlCodes:
        s = s.replace(code[1].encode('utf-8'), code[0].encode('utf-8'))
    return s.decode('utf-8')
def channel_Youtube(link_url,icon,image):
  
   import datetime
   headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers',
    }
   #tv_mode=__settings__.getSetting(id = 'deviceId')
   list=[]
   names=[]
   
   x=0
   all_d=[]
   addDir3('[COLOR khaki][B]All videos[/B][/COLOR]',link_url,9,icon,image,'YOUTUBE')
   xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
   page = requests.get(link_url,headers=headers).content

   matche = re.compile('ytInitialData = (.+?)};',re.DOTALL).findall(page.decode('utf-8'))
  
   all_j=json.loads(matche[0]+'}')
   
   for items in all_j['contents']['twoColumnBrowseResultsRenderer']['tabs'][0]['tabRenderer']['content']['sectionListRenderer']['contents']:
    if 'itemSectionRenderer' not in items:
        continue
    if 'shelfRenderer' not in items['itemSectionRenderer']['contents'][0]:
        continue
    name=items['itemSectionRenderer']['contents'][0]['shelfRenderer']['title']['runs'][0]['text'].encode('utf8')
    addNolink( '[COLOR lightblue][I]'+name.decode('utf-8')+'[/I][/COLOR]', 'www',999,False, iconimage=icon,fanart=image)
    
    
    
    all_d=[]
    if 'horizontalListRenderer' not in (items['itemSectionRenderer']['contents'][0]['shelfRenderer']['content']):
        continue
    for itt in items['itemSectionRenderer']['contents'][0]['shelfRenderer']['content']['horizontalListRenderer']['items']:
        if 'gridVideoRenderer' not in itt:
            continue
        it2=itt['gridVideoRenderer']
        name_final=it2['title']['simpleText'].encode('utf8')
        #image=it2['richThumbnail']['movingThumbnailRenderer']['movingThumbnailDetails']['thumbnails'][0]['url']
        image=it2['thumbnail']['thumbnails'][0]['url']
        all_img=it2['thumbnail']['thumbnails']
        max_res=0
        for itt_img in all_img:
            if itt_img['width']>max_res:
                image=itt_img['url']
        #logging.warning(image)
        link=it2['videoId']
        
       
        
        
    

        

        
        list.append(link)
        names.append(html_decode(name_final))
        
        video_data={}
        video_data['title']=html_decode(name_final)
        video_data['icon']=image
        video_data['fanart']=image
        video_data['plot']=html_decode(name_final)+'-HebDub-'
        
        addLink(html_decode(name_final).encode('utf-8',errors='ignore').decode('utf-8'),'https://www.youtube.com/watch?v='+link,10,False,image,image,html_decode(name_final))
   
    
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
  
def channel_Youtube_videos(link_url,icon,image,next_page):
    o_image=image
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Origin': 'https://youtubemultidownloader.net',
        'Connection': 'keep-alive',
        'Referer': 'https://youtubemultidownloader.net/channel.html',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    params = (
        ('url', link_url+'/videos'),
        ('nextPageToken', next_page),
    )
    logging.warning(link_url+'/videos')
    logging.warning(next_page)
    r = requests.get('https://api.youtubemultidownloader.com/playlist', headers=headers, params=params).json()
    all_d=[]
    for itt in r['items']:
        image=itt['thumbnails']
        video_data={}
        video_data['title']=itt['title']  
        video_data['icon']=image
        video_data['fanart']=image
        video_data['plot']=itt['title']+'-HebDub-'
        link=itt['url']
        addLink(itt['title'].encode('utf-8',errors='ignore').decode('utf-8'),link,10,False,image,image,itt['title'].encode('utf-8',errors='ignore').decode('utf-8'))
   
    all_d.append(addDir3('[COLOR lightblue][I][B]עמוד הבא[/B][/I][/COLOR]',link_url,9,icon,o_image,'YOUTUBE',page=r['nextPageToken']))
   
    
params=get_params()

url=None
name=None
mode=0
iconimage=None
fanart=None
description=None
data=None
page=0
try:
        url=unque(params["url"])
except:
        pass
try:
        name=unque(params["name"])
except:
        pass
try:
        iconimage=unque(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=unque(params["fanart"])
except:
        pass
try:        
        description=unque(params["description"])
except:
        pass
try:        
        data=unque(params["data"])
except:
        pass
try:        
        page=unque(params["page"])
except:
        pass
logging.warning('mode:'+str(mode))
if mode==0 :
        main_menu()
elif mode==2:
    play_link(name,url,description)
elif mode==3:
    files_from(name,url)
elif mode==4:
    video_data(name,url)
elif mode==5:
    next_level(url,iconimage,fanart)
elif mode==6:
    populate(url)
elif mode==7:
    all_videos(url,iconimage,fanart)
elif mode==8:

    channel_Youtube(url,iconimage,fanart)
elif mode==9:
    channel_Youtube_videos(url,iconimage,fanart,page)
elif mode==10:
    play_youtube (url,name )
elif mode==11:
    files_from(name,url,source=True)
xbmcplugin.setContent(int(sys.argv[1]), 'movies')


xbmcplugin.endOfDirectory(int(sys.argv[1]))

