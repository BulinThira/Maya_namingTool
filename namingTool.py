# NamingTool.py - Python Script

# DESCRIPTION: Tool for naming basic models (except joints with hierarchy)
# REQUIRE: Python3
# AUTHOR: BulinThira - Github

import maya.cmds as mc

def NamingTool():
    if mc.window('RT_window', q=True, ex=True):
        mc.deleteUI('RT_window', window=True)
    mc.window('RT_window', title='Naming Tool')
    mc.columnLayout(adj=True)
    
    #RENAME#
    mc.frameLayout(label='Rename')
    mc.gridLayout( numberOfColumns=2, cellWidthHeight=(150, 25) )
    mc.text(label='\tName:  ')
    mc.textField('name_textField', w=200)
    mc.setParent('..')
    
    mc.gridLayout( nrc=(2,2), cellWidthHeight=(150, 25) )
    mc.text(label='\tPadding:  ')
    mc.intField('padding_textField', value=2, minValue=1, maxValue=4, step=1)
    mc.text(label='    ')
    mc.optionMenu('optionside', label='Side')
    mc.menuItem ('1', label='--')
    mc.menuItem ('2', label='Left')
    mc.menuItem ('3', label='Right')
    mc.setParent('..')
    
    mc.gridLayout( nrc=(2,2), cellWidthHeight=(150, 25) )
    mc.text ('suffix_nameframe_text', label='\tSuffix:  ')
    mc.textField ('suffix_nameframe_textField', w=200)
    mc.setParent('..')

    mc.button ('rename button', label='Rename', h=30, c=doRename)
    
    #SEARCH AND REPLACE#
    mc.frameLayout(label='Search and Replace')
    mc.gridLayout( nrc=(2,2), cellWidthHeight=(150, 25) )
    mc.text('search_text', label='\tSearch:  ')
    mc.textField ('search_textField', w=200)
    mc.text ('replace_text', label='\tReplace:  ')
    mc.textField ('replace_textField', w=200)
    mc.setParent('..')
  
    mc.button ('replace button', label='Replace', h=30, c=doReplace)
    
    #QUICK REPLACE#
    mc.frameLayout (label='Quick Replace', bgc=(0.1, 0.5, 0.5))
    mc.gridLayout( nrc=(2,2), cellWidthHeight=(170, 25) )
    mc.button('LtoR button', label="L -> R", h=30, c=doLtoR)
    mc.button('RtoL button', label="R -> L", h=30, c=doRtoL)
    mc.setParent('..')
    
    #ADD QUICK PREFIX AND SUFFIX#
    mc.frameLayout (label='Quick Prefix and Suffix', bgc=(0.1, 0.5, 0.5))
    mc.gridLayout( nrc=(2,5), cellWidthHeight=(70, 25) )
    mc.text("quickpre_text", label="\tPrefix:  ")
    mc.button('quickL button', label="L", h=30, c=doQuickL )
    mc.button('quickR button', label="R", h=30, c=doQuickR )
    mc.button('quickC button', label="C", h=30, c=doQuickC )
    mc.setParent('..')
    
    mc.gridLayout( nrc=(2,5), cellWidthHeight=(70, 25) )
    mc.text("quicksuf_text", label="\tPrefix:  ")
    mc.button('quickGEO button', label="geo", h=30, c=doQuickGEO )
    mc.button('quickGRP button', label="grp", h=30, c=doQuickGRP )
    mc.button('quickJNT button', label="jnt", h=30, c=doQuickJNT )
    mc.button('quickCTRL button', label="ctrl", h=30, c=doQuickCTRL )
    mc.setParent('..')
    
    #ADD PREFIX AND SUFFIX#
    mc.frameLayout(label='Add Prefix amd Suffix')
    mc.gridLayout( nrc=(2,2), cellWidthHeight=(150, 25) )
    mc.text("pre_text", label="\tPrefix:  ")
    mc.textField("pre_textField", w=200)
    mc.text("suf_text", label="\tSuffix:  ")
    mc.textField("suf_textField", w=200)
    mc.setParent('..')

    mc.button ('addpresuf_button', label='Add', h=30, c=doAddPreSuf)
    
    mc.showWindow('RT_window')
    mc.window('RT_window', e=True, wh=(350,560))
    

def doRename(*args):

    name = mc.textField('name_textField', q=True, tx=True)
    padding = mc.intField('padding_textField', q=True, value=True)
    side = mc.optionMenu('optionside', q=True, value=True)
    suffix = mc.textField('suffix_nameframe_textField', q=True, tx=True)
    #suffix_nameframe = f'_{suffix}'
    sidename = ''
    
    
    if(side == '1'):
        sidename = False
    elif(side == '2'):
        sidename = 'L'
    elif(side == '3'):
        sidename = 'R'
        
    sels = mc.ls(sl=True)
    for i, each in enumerate(sels):
        padPat = f'%0{padding}d'
        
        if sidename:
            if suffix:
                newname = f'{name}_{padPat%(i+1)}_{side}_{suffix}'
            else:
                newname = f'{name}_{padPat%(i+1)}_{side}'
        else:
            if suffix:
                newname = f'{name}_{padPat%(i+1)}_{suffix}'
            else:
                newname = f'{name}_{padPat%(i+1)}'
    
        if newname:
            cmds.rename(each, newname)
    
def doReplace(*args):
    search = mc.textField('search_textField', q=True, tx=True)
    replace = mc.textField('replace_textField', q=True, tx=True)
    
    sels = mc.ls(sl=True)
    
    for each in sels:
        newname = each.replace(search, replace)
        mc.rename(each, newname)
        
def doLtoR(*args):
    sels_QPS = mc.ls(sl=True)
    for each in sels_QPS:
        newname_LR = each.replace('L', 'R')
        mc.rename(each, newname_LR)
        
def doRtoL(*args):
    sels_QPS = mc.ls(sl=True)
    for each in sels_QPS:
        newname_LR = each.replace('R', 'L')
        mc.rename(each, newname_LR)
        
def doQuickL(*args):
    sels_QPS = mc.ls(sl=True)
    for each in sels_QPS:
        newname_L = f'{"L" + "_" + each}'
        mc.rename(each, newname_L)
        
def doQuickR(*args):
    sels_QPS = mc.ls(sl=True)
    for each in sels_QPS:
        newname_R = f'{"R" + "_" + each}'
        mc.rename(each, newname_R)
        
def doQuickC(*args):
    sels_QPS = mc.ls(sl=True)
    for each in sels_QPS:
        newname_C = f'{"C" + "_" + each}'
        mc.rename(each, newname_C)
        
def doQuickGEO(*args):
    sels_QPS = mc.ls(sl=True)
    for each in sels_QPS:
        newname_GEO = f'{each + "_" + "geo"}'
        mc.rename(each, newname_GEO)
        
def doQuickGRP(*args):
    sels_QPS = mc.ls(sl=True)
    for each in sels_QPS:
        newname_GRP = f'{each + "_" + "grp"}'
        mc.rename(each, newname_GRP)
        
def doQuickJNT(*args):
    sels_QPS = mc.ls(sl=True)
    for each in sels_QPS:
        newname_JNT = f'{each + "_" + "jnt"}'
        mc.rename(each, newname_JNT)
        
def doQuickCTRL(*args):
    sels_QPS = mc.ls(sl=True)
    for each in sels_QPS:
        newname_CTRL = f'{each + "_" + "ctrl"}'
        mc.rename(each, newname_CTRL)
        
def doAddPreSuf(*args):
    prefixadd = mc.textField('pre_textField', q=True, tx=True)
    suffixadd = mc.textField('suf_textField', q=True, tx=True)
    
    sels = mc.ls(sl=True)
    
    for each in sels:
        if(prefixadd == ""):
            newname = f'{each + "_" + suffixadd}'
            mc.rename(each, newname)
        elif(suffixadd == ""):
            newname = f'{prefixadd +  "_" + each}'
            mc.rename(each, newname)
        else:
            newname = f'{prefixadd +  "_" + each +  "_" + suffixadd}'
            mc.rename(each, newname)
    
    
NamingTool()