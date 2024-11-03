from github import Github
import os

# GitHub setup
g = Github(os.getenv('GITHUB_TOKEN'))

def setup(bot):
    @bot.command()
    async def search_repo(ctx, query):
        """Search GitHub repositories"""
        repos = g.search_repositories(query)
        response = "Top 5 repositories:\n"
        for repo in repos[:5]:
            response += f"{repo.name}: {repo.html_url}\n"
        await ctx.send(response)

    @bot.command()
    async def create_gist(ctx, *, content):
        """Create a GitHub gist"""
        user = g.get_user()
        gist = user.create_gist(public=True, files={"file.txt": Github.InputFileContent(content)})
        await ctx.send(f"Gist created: {gist.html_url}")