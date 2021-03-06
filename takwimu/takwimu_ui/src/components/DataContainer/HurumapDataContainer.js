/* eslint-disable react/no-danger */
import React, { Fragment } from 'react';
import { PropTypes } from 'prop-types';

import { withTheme } from '@material-ui/core/styles';

import DataActions from './DataActions';
import IFrame from './IFrame';
import { shareIndicator, uploadImage } from './common';

function DataContainer({ id, data, theme, countryName }) {
  const iframeId = `cr-embed-country-${data.data_country}-${data.data_id}`;

  const toPng = () => {
    const iframe = document.getElementById(iframeId);
    const columnSets = iframe.contentDocument.getElementsByClassName(
      'column-set'
    );
    if (columnSets && columnSets.length) {
      columnSets[0].style.overflow = 'visible';
    }
    return iframe.contentWindow.domtoimage
      .toPng(iframe.contentDocument.getElementById('census-chart'), {
        bgcolor: theme.palette.data.light
      })
      .then(dataURL => {
        if (columnSets && columnSets.length) {
          columnSets[0].style.overflow = 'auto hidden';
        }
        return dataURL;
      });
  };

  const handleShare = () => {
    toPng().then(dataURL => {
      uploadImage(id, dataURL).then(success => {
        if (success) {
          shareIndicator(id);
        }
      });
    });
  };

  const handleDownload = () => {
    toPng().then(dataURL => {
      const link = document.createElement('a');
      link.download = `${data.title}.png`;
      link.target = '_blank';
      link.href = dataURL;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    });
  };

  const embedCode = `<iframe
    allowFullScreen
    title="${data.title}"
    src="/embed/iframe.html?geoID=country-${
      data.data_country
    }&geoVersion=2009&chartDataID=${data.data_id}&dataYear=2011&chartType=${
    data.chart_type
  }&chartHeight=300&chartTitle=${data.title}&initialSort=&statType=${
    data.data_stat_type
  }&chartSourceLink=${data.data_source_link}&chartSourceTitle=${
    data.data_source_title
  }&chartQualifier=${
    data.chart_qualifier
      ? data.chart_qualifier.replace('<br/>', '%0A').replace(/<(.|\n)*?>/g, '')
      : ''
  }&stylesheet=/static/css/embedchart.css"
/>`;

  return (
    <Fragment>
      <IFrame id={iframeId} data={data} />

      <DataActions
        title={`${countryName}: ${data.title}`}
        onDownload={handleDownload}
        embedCode={embedCode}
        onShare={handleShare}
      />
    </Fragment>
  );
}

DataContainer.propTypes = {
  theme: PropTypes.shape({}).isRequired,
  data: PropTypes.shape({}).isRequired,
  id: PropTypes.string.isRequired,
  countryName: PropTypes.string.isRequired
};

export default withTheme()(DataContainer);
