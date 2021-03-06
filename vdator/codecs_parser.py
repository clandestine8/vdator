# define codecs
class CodecsParser():
  """
  Define codecs
  """
  
  def __init__(self):
    # map codec names to extension
    self.video_codecs = {
      'h264/AVC' : '.h264',
      'h265/HEVC' : '.h265',
      'MPEG1' : '.m1v',
      'MPEG2' : '.m2v',
      'VC-1' : '.vc1',
    }

    self.audio_codecs = {
      'AC3' : '.ac3',
      'AC3 EX' : '.ac3',
      'AC3 Surround' : '.ac3',
      'DTS Master Audio' : '.dtsma',
      'DTS' : '.dts',
      'E-AC3' : 'eac3',
      'FLAC Audio' : '.flac',
      'RAW/PCM' : '.pcm',
      'TrueHD/AC3' : '.thd+ac3',
      'TrueHD/AC3 (Atmos)' : '.thd+ac3',
    }

    self.sub_codecs = {
      'Subtitle (PGS)' : '.sup',
      'Subtitle (DVD)' : '.sup',
    }

    self.chapter_codecs = {
      'Chapters' : '.txt',
    }
    
    # map codec names used in track title to names used in file title
    self.video_codec_title_names = {
      'MPEG-2 Video' : 'MPEG-2',
      'MPEG-4 AVC Video' : 'AVC',
      'MPEG-H HEVC Video' : 'HEVC',
      'VC-1 Video' : 'VC-1',
    }
    
    self.audio_codec_title_names = {
      'DTS Audio' : 'DTS',
      'DTS-HD Master Audio' : 'DTS-HD.MA',
      'DTS:X Master Audio' : 'DTS-X',
      'Dolby Digital Audio' : 'DD',
      'Dolby Digital EX Audio' : 'DD-EX',
      'Dolby TrueHD Audio' : 'TrueHD',
      'Dolby TrueHD/Atmos Audio' : 'TrueHD.Atmos',
      'FLAC Audio' : 'FLAC',
    }
    
    self.scan_type_title_names = {
      'interlaced' : 'i',
      'mbaff' : 'i',
      'progressive' : 'p',
    }

    # map of all codec names to extensions
    self.codec_ext = {**self.video_codecs, **self.audio_codecs, **self.sub_codecs, **self.chapter_codecs}

  def is_video(self, codec):
    """
    Is this a video codec?
    
    Parameters
    ----------
    codec : str
      codec
      
    Returns
    -------
    True if codec is a video codec, False otherwise.
    """
    if codec in self.video_codecs:
      return True
    return False
    
  def is_video_title(self, codec):
    """
    Is this a video title codec?
    
    Parameters
    ----------
    codec : str
      codec
      
    Returns
    -------
    True if codec is a video title codec, False otherwise.
    """
    if codec in self.video_codec_title_names:
      return True
    return False
    
  def is_audio(self, codec):
    """
    Is this an audio codec?
    
    Parameters
    ----------
    codec : str
      codec
      
    Returns
    -------
    True if codec is an audio codec, False otherwise.
    """
    if codec in self.audio_codecs:
      return True
    return False
    
  def is_audio_title(self, codec):
    """
    Is this an audio title codec?
    
    Parameters
    ----------
    codec : str
      codec
      
    Returns
    -------
    True if codec is an audio title codec, False otherwise.
    """
    if codec in self.audio_codec_title_names:
      return True
    return False
    
  def is_sub(self, codec):
    """
    Is this a subtitle codec?
    
    Parameters
    ----------
    codec : str
      codec
      
    Returns
    -------
    True if codec is a subtitle codec, False otherwise.
    """
    if codec in self.sub_codecs:
      return True
    return False

  def is_chapter(self, codec):
    """
    Is this a chapter codec?
    
    Parameters
    ----------
    codec : str
      codec
      
    Returns
    -------
    True if codec is a chapter codec, False otherwise.
    """
    if codec in self.chapter_codecs:
      return True
    return False
    
  def is_codec(self, codec):
    """
    Is this a valid codec?
    
    Parameters
    ----------
    codec : str
      codec
      
    Returns
    -------
    True if valid codec, False otherwise.
    """
    return codec in self.codec_ext
    
  def get_codec_ext(self, codec):
    """
    Get codec extension. Checks if codec is valid.
    
    Parameters
    ----------
    codec : str
      codec
      
    Returns
    -------
    str codec extension
    """
    if codec not in self.codec_ext:
      return ''
    return self.codec_ext[codec]
    
  def get_video_codec_title_name(self, codec):
    """
    Get name of video codec for title. Checks if video codec is valid.
    
    Parameters
    ----------
    codec : str
      codec
      
    Returns
    -------
    str codec title name
    """
    if codec not in self.video_codec_title_names:
      return ''
    return self.video_codec_title_names[codec]
    
  def get_audio_codec_title_name(self, codec):
    """
    Get name of audio codec for title. Checks if audio codec is valid.
    
    Parameters
    ----------
    codec : str
      codec
      
    Returns
    -------
    str codec title name
    """
    if codec not in self.audio_codec_title_names:
      return ''
    return self.audio_codec_title_names[codec]
    
  def get_scan_type_title_name(self, scan_type, video_fps):
    """
    Get name of video scan type for title. Checks if scan type is valid.
    
    Parameters
    ----------
    scan_type : str
      scan type
      
    video_fps : str
      frame rate
      
    Returns
    -------
    str scan type title name, boolean if actually progressive
    """
    actually_progressive = False
    scan_type = scan_type.strip()
    
    if len(scan_type) == 1:
      scan_type = 'progressive' if scan_type == 'p' else 'interlaced'

    # interlaced @ 25fps is actually progressive
    # but it's still called interlaced
    if scan_type == 'interlaced' and int(video_fps) == 25:
      #scan_type = 'progressive'
      actually_progressive = True
      
    if scan_type not in self.scan_type_title_names:
      return ''
    return self.scan_type_title_names[scan_type], actually_progressive
    
