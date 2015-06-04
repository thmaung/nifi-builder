#!/usr/bin/rake -T

# For playing nice with mock
File.umask(027)

require 'simp/rake/pkg'

#begin
#  require 'puppetlabs_spec_helper/rake_tasks'
#rescue LoadError
#  puts "== WARNING: Gem puppetlabs_spec_helper not found, spec tests cannot be run! =="
#end

simp = Simp::Rake::Pkg.new( File.dirname( __FILE__ ) )

namespace :build do
  desc <<-EOM
  Build the #{simp.pkg_name} rpm from input tar file location.
      * :src_tar - Source tar file
  EOM
  task :rpm,[:src_tar,:chroot,:unique,:snapshot_release] => [simp.pkg_dir] do |t,args|
    args.with_defaults(:unique => false)
    args.with_defaults(:snapshot_release => false)

    @spec_info      = Simp::Rake::Pkg.get_info( simp.spec_file )
    @chroot_name    = @chroot_name || "#{@spec_info[:name]}__#{ENV.fetch( 'USER', 'USER' )}"
    @dir_name       = "#{@spec_info[:name]}-#{@spec_info[:version]}"
    @mfull_pkg_name = "#{@dir_name}-#{@spec_info[:release]}"
    @full_pkg_name  = @mfull_pkg_name.gsub("%{?snapshot_release}","")
    @tar_dest       = "#{simp.pkg_dir}/#{@full_pkg_name}.tar.gz"

    l_date = ''
    if args.snapshot_release == 'true' then
      l_date = '.' + "#{TIMESTAMP}"
      mocksnap = "-D 'snapshot_release #{l_date}'"
      @tar_dest = "#{simp.pkg_dir}/#{@full_pkg_name}#{l_date}.tar.gz"
    end

    # Copy Tar
    sh %Q{/bin/cp #{args.src_tar} #{@tar_dest}} 

    # Buid SRPM
    mock_cmd = simp.mock_pre_check( args.chroot, @chroot_name, args.unique )
    output = "#{@full_pkg_name}#{l_date}.src.rpm"
    if not uptodate?("#{simp.pkg_dir}/#{output}",[@tar_dest]) then
      cmd = %Q{#{mock_cmd} --verbose --no-clean --root #{args.chroot} #{mocksnap} --buildsrpm --spec #{simp.spec_file} --source #{simp.pkg_dir}}
      sh cmd
    end

    # Build RPM
    output = "#{@full_pkg_name}#{l_date}.#{@spec_info[:arch]}.rpm"
    if not uptodate?("#{simp.pkg_dir}/#{output}",[@tar_dest]) then
      cmd = %Q{#{mock_cmd} --verbose --root #{args.chroot} #{mocksnap} #{simp.pkg_dir}/#{@full_pkg_name}#{l_date}.src.rpm}
      sh cmd
    end
  end
end
