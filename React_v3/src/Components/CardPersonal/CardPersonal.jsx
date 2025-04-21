import React from 'react'
import './CardPersonal.css'
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

const CardPersonal = (props) => {
    return (
        <Card sx={{ maxWidth: 345 }}>
            <CardMedia
                component="img"
                image={props.image}
            />
            <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                    {props.name}
                </Typography>
                <Typography variant="body2" sx={{ color: "text.secondary" }}>
                    {props.name}
                </Typography>

            </CardContent>
            <CardActions>
                <Button size="small">Share</Button>
                <Button size="small">Learn More</Button>
            </CardActions>
        </Card>)
}

export default CardPersonal