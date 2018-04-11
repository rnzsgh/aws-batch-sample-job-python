import boto3, os

def main():
    """ A very simple test that showcases generating random data and then writing it to
    an S3 bucket. Your container must have permission to write to the S3 bucket that
    is provided as an environment variable. """
    print 'Hello world'

    print 'Generating test data'
    with open('output_file', 'wb') as fout:
        fout.write(os.urandom(49152))
        fout.close()

    print 'Push test data to S3'
    s3_client = boto3.resource('s3')

    with open('output_file', 'rb') as data:
        s3_client.Bucket(os.environ['S3_BUCKET_NAME']).put_object(Key='output_file', Body=data)
        data.close()

if __name__ == '__main__':
    main()
