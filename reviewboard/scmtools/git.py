        super(GitTool, self).__init__(repository)

        local_site_name = None

        if repository.local_site:
            local_site_name = repository.local_site.name

        self.client = GitClient(repository.path, repository.raw_file_url,
                                local_site_name)
    def check_repository(cls, path, username=None, password=None,
                         local_site_name=None):
        client = GitClient(path, local_site_name=local_site_name)
        super(GitTool, cls).check_repository(client.path, username, password,
                                             local_site_name)
    def __init__(self, path, raw_file_url=None, local_site_name=None):
        self.local_site_name = local_site_name
        return SCMTool.popen(['git'] + args,
                             local_site_name=self.local_site_name)
            return 'ssh://%s%s%s' % (m.group('username') or '',