import os, re

# 'mediainfo' to use mediainfo fields
# 'nobdinfo' to assume DVD if no bdinfo given
DVD_CHECK_MODE = os.environ.get("DVD_CHECK_MODE").strip()

# detect if DVD, 1080p BluRay or UHD BluRay
class SourceDetector():
  """
  Define ways to detect source
  """
  
  def __init__(self, bdinfo, mediainfo):
    """    
    Parameters
    ----------
    bdinfo : dict
      bdinfo
      
    mediainfo : dict
      mediainfo
    """
    self.bdinfo = bdinfo
    self.mediainfo = mediainfo

  def is_dvd(self):
    """
    Is this source a DVD?
      
    Returns
    -------
    boolean True if DVD, False otherwise
    """
    is_dvd = False
    
    if DVD_CHECK_MODE == 'nobdinfo':
      if not self._has_bdinfo():
        # no bdinfo given, assume dvds
        is_dvd = True
    elif DVD_CHECK_MODE == 'mediainfo':
      if 'video' in self.mediainfo and len(self.mediainfo['video']) >= 1 \
        and 'height' in self.mediainfo['video'][0]:
          height = int(''.join(re.findall(r'[\d]+', self.mediainfo['video'][0]['height'])))
          if height <= 576:
            # height is 480p or 576p for dvds
            # Note: checking standard is NTSC or PAL won't work, as some BDs are NTSC
            is_dvd = True
    
    return is_dvd
    
  def is_uhd(self):
    """
    Is this source a UHD BluRay?
      
    Returns
    -------
    boolean True if UHD, False otherwise
    """
    is_uhd = False
    
    if 'video' in self.mediainfo and len(self.mediainfo['video']) >= 1 \
      and 'height' in self.mediainfo['video'][0]:
        height = int(''.join(re.findall(r'[\d]+', self.mediainfo['video'][0]['height'])))
        if height == 2160:
          is_uhd = True
    
    return is_uhd
    
  def _has_bdinfo(self):
    """
    Does the paste include bdinfo?
      
    Returns
    -------
    boolean True if has bdinfo, False otherwise
    """
    has_bdinfo = False
    
    if len(self.bdinfo['video']) == 0 and len(self.bdinfo['audio']) == 0 and len(self.bdinfo['subtitle']) == 0:
      has_bdinfo = False
    else:
      has_bdinfo = True
      
    return has_bdinfo
    