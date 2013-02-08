require 'yaml'
require 'fileutils'

desc "Prepare the package"
task :prepare, [:version] do |task,args|
  config = YAML.load_file('config.yml')

  sh "echo #{args.version} > VERSION"

  # prepare dirs
  FileUtils.mkdir 'packages'
  FileUtils.mkdir_p 'workdir/doc/check_mk/checks' unless Dir.exists?('workdir/doc/check_mk/checks')
  FileUtils.mkdir_p 'workdir/check_mk/checks' unless Dir.exists?('workdir/check_mk/checks')

  # copy files
  FileUtils.cp_r 'checks/.', 'workdir/check_mk/checks/'
  FileUtils.cp_r 'doc/.', 'workdir/doc/check_mk/checks/'

end

desc 'Build the package'
task :build do
  config = YAML.load_file('config.yml')

  version = File.read('VERSION').strip
  version += "-#{ENV['BUILD_NUMBER']}" if ENV['BUILD_NUMBER']

  Dir.chdir 'workdir'
  sh "fpm \
-s dir \
-t deb \
-n #{config['package_name']} \
--prefix #{config['package_prefix']} \
-v #{version} \
-a all \
--description \"#{config['package_description']}\" \
--url \"#{config['package_website']}\" \
."

  Dir.chdir '..'
  sh "mv workdir/#{config['package_name']}_#{version}_all.deb packages/"

end

desc "Cleanup prepare dirs"
task :clean do
  FileUtils.rm 'VERSION' if File.exists? 'VERSION'
  FileUtils.rm_r 'packages' if File.exists? 'packages'
  FileUtils.rm_r 'workdir' if File.exists? 'workdir'
end
