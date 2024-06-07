import click
import os
import gzip

@click.command()
@click.option('--feed-folder-path', type=click.Path(exists=True), help='Path to the feed folder')
@click.option('--old-base-url', help='base URL to be replaced')
@click.option('--new-base-url', help='new base URL of packages')

def cli(feed_folder_path, old_base_url, new_base_url):
    click.echo(f'Feed path: {feed_folder_path}')
    click.echo(f'Package local path: {old_base_url}')
    click.echo(f'Package URL: {new_base_url}')
    
    packages_file_path = os.path.join(feed_folder_path, 'Packages')
    replace_url(packages_file_path, old_base_url, new_base_url)
    packagesStamps_file_path = os.path.join(feed_folder_path, 'Packages.stamps')
    replace_url(packagesStamps_file_path, old_base_url, new_base_url)
    compress_packages_file(feed_folder_path)

def replace_url(file_path, old_url, new_url):
    
    with open(file_path, 'r') as f:
        content = f.read()

    # Replace the old string with the new string
    updated_content = content.replace(old_url, new_url)

    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.write(updated_content)    

def compress_packages_file(feed_path):
    with open(os.path.join(feed_path, 'Packages'), 'rb') as f_in:
        with gzip.open(os.path.join(feed_path, 'Packages.gz'), 'wb') as f_out:
            f_out.writelines(f_in)

if __name__ == "__main__":
    cli()