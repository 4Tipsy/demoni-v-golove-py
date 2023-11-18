





async def play_track(message, raw_url):
    

  ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
      'key': 'FFmpegExtractAudio',
      'preferredcodec': 'mp3',
      'preferredquality': '192',
    }],
  }

  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(raw_url, download=False)
    url2 = info['formats'][0]['url']
    voice_client = message.guild.voice_client.voice_client

    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn',
    }

    voice_client.stop()
    await voice_client.play(discord.FFmpegPCMAudio(url2, **FFMPEG_OPTIONS))
    del current_music_queue["queue"][0]