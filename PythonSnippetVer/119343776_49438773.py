bot = commands.Bot('>')

@bot.command(pass_context = True)
@commands.has_role('admin')
async def Say(ctx, *args):
    mesg = ' '.join(args)
    await bot.delete_message(ctx.message)
    return await bot.say(mesg)

bot.run('Token')