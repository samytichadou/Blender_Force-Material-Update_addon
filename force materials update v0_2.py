# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; version 3
#  of the License.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {  
 "name": "Force Materials Update",  
 "author": "Sammey, Samy Tichadou (tonton)",  
 "version": (0, 2),  
 "blender": (2, 7, 9),  
 "location": "3d View > Down Header",  
 "description": "Force update of viewport materials",  
  "wiki_url": "https://blenderartists.org/forum/showthread.php?399511-Force-material-update-OpenGL-render-active-viewport",  
 "tracker_url": "https://blenderartists.org/forum/showthread.php?399511-Force-material-update-OpenGL-render-active-viewport",  
 "category": "3D View"}

import bpy
from bpy.app.handlers import persistent

#######################################################################
### HANDLER ###
#######################################################################

@persistent
def force_update_materials_handler(scene):
    if bpy.data.window_managers['WinMan'].force_update_materials == True:
        mats = bpy.data.materials
        for m in mats:
            if m.invert_z==True:
                m.invert_z==True
            else:
                m.invert_z = False
            
            
#######################################################################
### GUI ###
#######################################################################

def force_update_menu_draw(self, context):
    winman=bpy.data.window_managers['WinMan']

    layout = self.layout
    row = layout.row(align=True)
    row.prop(winman, 'force_update_materials', text='', icon='IMAGE_RGB')


#######################################################################
### reg/unreg ###
#######################################################################
            
def register():
    bpy.app.handlers.frame_change_pre.append(force_update_materials_handler)
    
    bpy.types.WindowManager.force_update_materials = \
        bpy.props.BoolProperty(default=False,
                                description="Toggle On/Off Force Update Materials in the Viewport")
                                
    bpy.types.VIEW3D_HT_header.append(force_update_menu_draw)

                                
def unregister():
    bpy.app.handlers.frame_change_pre.remove(force_update_materials_handler)
    
    del bpy.types.WindowManager.force_update_materials

    bpy.types.VIEW3D_HT_header.remove(force_update_menu_draw)

    
if __name__ == "__main__":
    register()