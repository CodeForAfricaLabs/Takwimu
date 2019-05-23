/* eslint-disable react/no-danger */
import React, { Fragment } from 'react';
import { PropTypes } from 'prop-types';

import { withStyles } from '@material-ui/core';

import DataActions from './DataActions';
import { shareIndicator, uploadImage } from './common';

const styles = {
  root: {
    width: '100%'
  }
};

function DataContainer({ id, classes, data }) {
  const toCanvas = () => {
    const iframe = document.getElementById(`data-indicator-${id}`);
    return iframe.contentWindow.html2canvas(iframe.contentDocument.body);
  };
  const handleDownload = () => {
    toCanvas().then(canvas => {
      const link = document.createElement('a');
      link.download = `${data.title}.png`;
      link.target = '_blank';
      link.href = canvas.toDataURL('image/png');
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    });
  };

  const handleShare = () => {
    toCanvas().then(canvas => {
      uploadImage(id, canvas.toDataURL('image/png')).then(success => {
        if (success) {
          shareIndicator(id);
        }
      });
    });
  };

  const handleIframeLoaded = e => {
    const iframe = e.target;
    const { offsetHeight } =
      iframe.contentDocument.getElementById('wrapper') ||
      iframe.contentDocument.body;
    iframe.style.height = `${offsetHeight}px`;

    // Add htm2canvas
    const frameHead = iframe.contentDocument
      .getElementsByTagName('head')
      .item(0);
    const script = iframe.contentDocument.createElement('script');
    script.type = 'text/javascript';
    script.src =
      'https://cdn.jsdelivr.net/npm/html2canvas@1.0.0-rc.1/dist/html2canvas.min.js';
    frameHead.appendChild(script);
  };

  const embedCode = `<iframe title="${data.title}" 
  frameborder="0" 
  scrolling="no" 
  src="https://takwimu.africa/flourish/${data.html}" />`;

  return (
    <Fragment>
      <iframe
        id={`data-indicator-${id}`}
        frameBorder="0"
        scrolling="no"
        title={data.title}
        src={`/flourish/${data.html}`}
        onLoad={handleIframeLoaded}
        className={classes.root}
      />
      <DataActions
        onDownload={handleDownload}
        embedCode={embedCode}
        onShare={handleShare}
      />
    </Fragment>
  );
}

DataContainer.propTypes = {
  id: PropTypes.string,
  classes: PropTypes.shape({}).isRequired,
  data: PropTypes.shape({}).isRequired
};

DataContainer.defaultProps = {
  id: ''
};

export default withStyles(styles)(DataContainer);
