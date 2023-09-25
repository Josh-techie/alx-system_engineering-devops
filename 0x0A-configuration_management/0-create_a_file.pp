# Task 0: Create a file
file { '/tmp/school':
	  ensure  => file,         # Ensure it's a file
		    mode    => '0744',       # Set file permissions to 0744
		      owner   => 'www-data',   # Set the owner to www-data
		        group   => 'www-data',   # Set the group to www-data
			  content => 'I love Puppet',  # Set the file content
}
