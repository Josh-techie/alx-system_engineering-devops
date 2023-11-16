ky_is_the_limit_not.pp

# This Puppet manifest optimizes Nginx settings to handle high traffic.

# Increase the ULIMIT of the default file
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart Nginx
exec { 'nginx-restart':
  command => 'service nginx restart',
  path    => '/etc/init.d/',
  onlyif  => 'test -f /etc/init.d/nginx', # Ensure the file exists before restarting
}
