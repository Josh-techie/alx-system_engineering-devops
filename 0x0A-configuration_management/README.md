## Configuration Management (CM):

- CM involves managing system changes using automation tools like Puppet, Ansible, Chef, or Salt.
- Benefits include fast server setup, quick recovery, and consistency.
- CM tools typically use a master-controller and agent-node setup.
- When selecting a tool, consider factors like complexity, cost, and community support.

## Puppet "file" Resource:

- Puppet's "file" resource manages files, including their content, permissions, and more.
- Utilize attributes such as `path`, `ensure`, and `content` to control files.
- Puppet can back up files and uses checksums to decide when to replace them.
- It's capable of managing directories and handling SELinux attributes.

## Puppet-lint Tool:

- Puppet-lint checks if your Puppet code adheres to a style guide.
- Installation can be done via Puppet or the gem command.
- Run it on your Puppet code to ensure it aligns with style guidelines.
- Puppet-lint can also automatically correct some code issues.

## Ressources:
* [Intro TO CM] (https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)
* [Attributes:File] (https://www.puppet.com/docs/puppet/5.5/types/file.html)
* [Install Lint ](http://puppet-lint.com/)
* [Puppet Checker Repo] (https://github.com/voxpupuli/puppet-mode)

## Author:
- [Josh-Techie](https://github.com/Josh-techie)
