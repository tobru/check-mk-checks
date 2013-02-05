require 'yaml'
require 'fileutils'

desc "Prepare the package"
task :prepare, [:version] do |task,args|
  config = YAML.load_file('config.yml')

  sh "echo #{args.version} > VERSION"

  Dir.mkdir 'packages' unless Dir.exists?("packages")

end

desc 'Build the package'
task :build do
  config = YAML.load_file('config.yml')

  version = File.read('VERSION').strip
  version += "-#{ENV['BUILD_NUMBER']}" if ENV['BUILD_NUMBER']

  Dir.chdir 'checks'
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
  sh "mv checks/#{config['package_name']}_#{version}_all.deb packages/"

end

desc "Cleanup prepare dirs"
task :clean do
  FileUtils.rm 'VERSION' if File.exists? 'VERSION'
  FileUtils.rm_r 'packages' if File.exists? 'packages'
end
