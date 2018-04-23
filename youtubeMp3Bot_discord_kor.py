import discord
import pytube
import os
import subprocess
import asyncio

from discord import User

client = discord.Client()
commend = '!위버 '
rootName = 'Wiber'

S_ID = 'your_token'

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith(commend + '테스트'):
        await client.send_message(message.channel, '{0.author.mention}'.format(message) + '위버봇 현재 작동중~ (>▽<)/')

    elif message.content.startswith(commend + "help"):
        await client.send_message(message.channel, '기본적으로 명령어 앞에는 "!위버"를 붙여 ex)!위버 테스트!')
        await client.send_message(message.channel, 'help : 명령어 보기')
        await client.send_message(message.channel, '테스트 : 제대로 작동하는지 테스트 하는거')
        await client.send_message(message.channel, '!!! : 위버를 부르는 명령어!')
        await client.send_message(message.channel, '다운로드 : 유튜브에 있는 영상을 mp3파일로 변환해 주는거')
        return

    elif message.content.startswith(commend + "!!!"):
        await client.send_message(message.channel, '{0.author.mention}'.format(message) + '왜?  [도와줘, 하이~, 뭐해?]')
        msg = await client.wait_for_message(timeout=10.0, author=message.author)

        if msg is None:
            await client.send_message(message.channel, '{0.author.mention}'.format(message) + '10초내로 말해주세요!! (>△<)/')
            return
        else:
            if msg.content == '도와줘':
                await client.send_message(message.channel, '기본적으로 명령어 앞에는 "!위버"를 붙여! ex)!위버 테스트')
                await client.send_message(message.channel, '테스트 : 제대로 작동하는지 테스트 하는거')
                await client.send_message(message.channel, '!!! : 위버를 부르는 명령어!')
                await client.send_message(message.channel, '다운로드 : 유튜브에 있는 영상을 mp3파일로 변환해서 주는거')
                return
            elif msg.content == '하이~':
                await client.send_message(message.channel, '하이~ (>▽<)/')
                return

            elif msg.content == '뭐해?':
                while (1):
                    answer = input('대답 : ')
                    if answer == '뭐해끝':
                        return
                    await client.send_message(message.channel, answer)
                return

    elif message.content.startswith(commend + '다운로드'):
        await client.send_message(message.channel,
                                  '{0.author.mention}'.format(message) + '다운받을 영상의 주소를 줘!(유튜브, 너무 긴거주면 뽀또맛콜라)')
        msg = await client.wait_for_message(timeout=10.0, author=message.author)

        if msg is None:
            await client.send_message(message.channel, '{0.author.mention}'.format(message) + '10초내로 말해주세요!! (>△<)/')
            return

        else:
            st = await client.wait_for_message(timeout=0.0, author=message.author)

            if st is None:
                yt = pytube.YouTube(msg.content)
                vids = yt.streams.all()

                path = "C:\\Users\\wiber\\pythonProject\\downloadYoutubeMp3\\"
                vids[0].download(path)
                fileName = vids[0].default_filename

                await client.send_message(message.channel, '{0.author.mention}'.format(message) + '잠깐만 기다려봐바(뒤적뒤적)')
                print(fileName)
                subprocess.call(['ffmpeg', '-i',
                                 os.path.join(path, fileName),
                                 os.path.join(path, fileName + '.mp3')
                                 ])

                await client.send_file(message.channel, path + fileName + '.mp3')
                await client.send_message(message.channel, "(>ㅅ<)/")

                os.remove(path + fileName)
                os.remove(path + fileName + '.mp3')

                return

    elif message.content.startswith(commend + '잘자~'):
        await client.send_message(message.channel, '안녕히 주무세요~(ㅇ~ㅇ)/')
        await client.logout()
        await client.close()
        return

    elif message.content.startswith(commend + '만든사람'):
        user = discord.utils.get(message.server.members, name=rootName)
        await client.send_message(message.channel, user.mention + '가 Rapptz/discord.py 를 사용하여 만들었습니다.')
        return

    elif message.content.startswith(commend + "호출"):
        user = discord.utils.get(message.server.members, name=rootName)
        await client.send_message(message.channel,
                                  '{0.author.mention}'.format(message) + '님이 ' + user.mention + '님을 호출하였습니다')
        return


client.run(S_ID)
