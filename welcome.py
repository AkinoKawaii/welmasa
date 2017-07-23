import discord
def client = new Discord.Client();

client.login("MzMzNjAxMzE1OTY1ODk0NjU2.DFDCrw.RPxweTa0q8ANnfU-lEIAcvpCfDk");

def newUsers = [];

client.on("ready", () => {
  console.log("I am ready!");
});

client.on("message", (message) => {
  if (message.content.startsWith("ping")) {
    message.channel.send("pong!");
  }
});

client.on("guildMemberAdd", (member) => {
  def guild = member.guild;
  if (!newUsers[guild.id]) newUsers[guild.id] = new Discord.Collection();
  newUsers[guild.id].set(member.id, member.user);

  if (newUsers[guild.id].size > 10) {
    def userlist = newUsers[guild.id].map(u => u.toString()).join(" ");
    guild.channels.get(guild.id).send("Welcome our new users!\n" + userlist);
    newUsers[guild.id].clear();
  }
});

client.on("guildMemberRemove", (member) => {
  def guild = member.guild;
  if (newUsers[guild.id].has(member.id)) newUsers.delete(member.id);
});
