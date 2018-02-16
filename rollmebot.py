import discord
import asyncio
from random import randint, choice
import sys

client = discord.Client()
msgs = ['pffff....', 'The spell fizzles...']

def roll(value):
	return randint(1, value)

def rollCharacter():
	sum = 0
	while sum < 70:
		sum = 0
		stats = []
		for i in range(6):
			stat = []
			for j in range(4):
				stat.append(roll(6))
			stat.remove(min(stat))
			v = 0
			for j in stat:
				v += j
			stats.append(v)
		for i in stats:
			sum += i
	
	s_stats = ''
	for i in stats:
		print(i)
		s_stats += str(i) + '\t'
	return s_stats

async def replyTo(message, reply):
	await client.send_message(message.channel, '<@'+ message.author.id + '>\t' + reply)
	
@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
async def on_message(message):
	try:
		if message.content.startswith('!h'):
			msg = '~ !roll or !r ~ Rolls a d20 and replies with value.\n~ !roll 2d4 5 -5 ~ Rolls 2d4 then adds 5 then subtracts 5, replying with the total.\n~ !roll2 or !r2 ~ Rolls 2 d20 and displays the result of each rool, use for dis/advantage.'
			await replyTo(message, msg)	
		elif message.content.startswith('!roll2') or message.content.startswith('!r2'):
			await replyTo(message, str(roll(20)) + '\t' + str(roll(20)))
		elif message.content.startswith('!r'):
			args = message.content.split()
			args.pop(0)
			if not args:
				await replyTo(message, str(roll(20)))
			elif args[0] == 'char':
				await replyTo(message, rollCharacter())
			else:
				total = 0
				for arg in args:
					if 'd' in arg:
						v = arg.split('d')
						if v[0] == '':
							total += roll(int(v[1]))
						else:
							for i in range(int(v[0])):
								total += roll(int(v[1]))
					elif arg.isdigit() or arg[0] == '-' and arg[1:].isdigit():
						total += int(arg)

				await replyTo(message, str(total))
		
		elif message.content.startswith('!test'):
			await client.send_message(message.channel, 'We\'re live!')
	except Exception as e:
		print(e)
		await client.send_message(message.channel, choice(msgs))

client.run('MzcwMDMyMjQ3NTM1MDQyNTYy.DMhvrQ.UaprWQb67WpV0fF5Hdqeej5fddk')

