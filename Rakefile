require 'yaml'
require 'fileutils'

desc "Prepare the package"
task :prepare, [:version] do |task,args|
  config = YAML.load_file('config.yml')

  sh "echo #{args.version} > VERSION"

  # prepare dirs
  FileUtils.mkdir 'packages'
  FileUtils.mkdir_p "workdir#{config['cmk_checks_dir']}" unless Dir.exists?("workdir#{config['cmk_checks_dir']}")
  FileUtils.mkdir_p "workdir#{config['cmk_checksdoc_dir']}" unless Dir.exists?("workdir#{config['cmk_checksdoc_dir']}")
  FileUtils.mkdir_p "workdir#{config['cmk_perfometer_dir']}" unless Dir.exists?("workdir#{config['cmk_perfometer_dir']}")
  FileUtils.mkdir_p "workdir#{config['cmk_pnptemplates_dir']}" unless Dir.exists?("workdir#{config['cmk_pnptemplates_dir']}")

  # copy files
  FileUtils.cp_r 'checks/.', "workdir#{config['cmk_checks_dir']}"
  FileUtils.cp_r 'doc/.', "workdir#{config['cmk_checksdoc_dir']}"
  FileUtils.cp_r 'perf-o-meter/.', "workdir#{config['cmk_perfometer_dir']}"
  FileUtils.cp_r 'pnp-templates/.', "workdir#{config['cmk_pnptemplates_dir']}"

end

desc "Prepare the package for OMD"
task :prepareomd, [:site] do |task,args|
  config = YAML.load_file('config.yml')

  # copy files
  FileUtils.cp_r 'checks/.', "/omd/sites/#{args.site}/#{config['omd_checks_dir']}"
  FileUtils.cp_r 'doc/.', "/omd/sites/#{args.site}/#{config['omd_checksdoc_dir']}"
  FileUtils.cp_r 'perf-o-meter/.', "/omd/sites/#{args.site}/#{config['omd_perfometer_dir']}"
  FileUtils.cp_r 'pnp-templates/.', "/omd/sites/#{args.site}/#{config['omd_pnptemplates_dir']}"

end

desc 'Build the package'
task :build, :pkgname do |task,args|
  config = YAML.load_file('config.yml')

  version = File.read('VERSION').strip
  version += "-#{ENV['BUILD_NUMBER']}" if ENV['BUILD_NUMBER']

  Dir.chdir 'workdir'
  sh "fpm \
-s dir \
-t deb \
-n #{args.pkgname} \
--prefix / \
-v #{version} \
-a all \
--description \"#{config['package_description']}\" \
--url \"#{config['package_website']}\" \
."

  Dir.chdir '..'
  sh "mv workdir/#{args.pkgname}_#{version}_all.deb packages/"

end

desc "Cleanup prepare dirs"
task :clean do
  FileUtils.rm 'VERSION' if File.exists? 'VERSION'
  FileUtils.rm_r 'packages' if File.exists? 'packages'
  FileUtils.rm_r 'workdir' if File.exists? 'workdir'
end
