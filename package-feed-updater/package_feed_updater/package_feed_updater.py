import click
import subprocess
import os
import time
import gzip

@click.command()
@click.option('--feed-path', type=click.Path(exists=True), help='Path to the feed file')
@click.option('--pkg-local-path', type=click.Path(exists=True), help='Path to the local package file')
@click.option('--pkg-url', help='URL to the package file')

def cli(feed_path, pkg_local_path, pkg_url):
    click.echo(f'Feed path: {feed_path}')
    click.echo(f'Package local path: {pkg_local_path}')
    click.echo(f'Package URL: {pkg_url}')
    
    add_package(feed_path, pkg_local_path)
    update_feed_with_url(feed_path, pkg_local_path, pkg_url)
    compress_packages_file(feed_path)

def add_package(feed_path, pkg_local_path):
    packages_file_path = os.path.join(feed_path, 'Packages')
    if not os.path.isfile(packages_file_path):
        subprocess.run(['C:\\Program Files\\National Instruments\\NI Package Manager\\nipkg.exe', 'feed-create', feed_path])
    subprocess.run(['C:\\Program Files\\National Instruments\\NI Package Manager\\nipkg.exe', 'feed-add-pkg', feed_path, pkg_local_path])

def update_feed_with_url(feed_path, pkg_local_path, pkg_url):
    package_name = os.path.basename(pkg_local_path)
    package_name = package_name.split('.')[0]
    package_name = package_name.lower()

    # Update the Packages file with URL
    with open(os.path.join(feed_path, 'Packages'), 'r') as f:
        lines = f.readlines()

    with open(os.path.join(feed_path, 'Packages'), 'w') as f:
        for line in lines:
            if line.startswith('Filename:'):
                if package_name in line.lower():
                    line = f'Filename: {pkg_url}\n'
            f.write(line)

    # Update the Packages.stamps file with URL
    with open(os.path.join(feed_path, 'Packages.stamps'), 'r') as f:
        lines = f.readlines()

    with open(os.path.join(feed_path, 'Packages.stamps'), 'w') as f:
        for line in lines:
            if package_name in line:
                line = f'{int(time.time())} {pkg_url}\n'
            f.write(line)

def compress_packages_file(feed_path):
    with open(os.path.join(feed_path, 'Packages'), 'rb') as f_in:
        with gzip.open(os.path.join(feed_path, 'Packages.gz'), 'wb') as f_out:
            f_out.writelines(f_in)

if __name__ == "__main__":
    cli()